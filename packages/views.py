from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Destination, Package, PackageType, Interest, Notification
from .serializers import (
    PackageSerializer,
    PackageTypeSerializer,
    PackageDetailSerializer,
    InterestSerializer,
    NotificationSerializer,
    PackageTitleSerializer,
    PackageTypeNavSerializer,
    PackageTypeHomeSerializer,
)

from rest_framework import generics
from django_filters import rest_framework as filters


def get_object_notify(slug):
    try:
        return Notification.objects.get(slug=slug)
    except Notification.DoesNotExist:
        raise Http404


def get_object(slug):
    try:
        return Package.objects.get(slug=slug)
    except Package.DoesNotExist:
        raise Http404


def get_object_id(pk):
    try:
        return Package.objects.get(pk=pk)
    except Package.DoesNotExist:
        raise Http404

def get_object_package_type(slug):
    try:
        return PackageType.objects.get(slug=slug)
    except Package.DoesNotExist:
        raise Http404

#Notification

class NotificationRetrieveApi(APIView):
    def get(self, request, slug):
        notification = get_object_notify(slug)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotificationListApi(APIView):
    def get(self, request):
        notifications = Notification.objects.all().filter(active=True)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Packages 

class PackageHomeListApi(APIView):
    def get(self, request):
        packages = Package.objects.all().filter(published=True, is_home=True)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PackageFeaturedDestinationListApi(APIView):
    def get(self, request, slug):
        packages = Package.objects.all().filter(published=True,destination__slug=slug, featured=True)[:6]
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PackageCitiesListApi(APIView):
    def get(self, request, slug, slug_destination):
        packages = Package.objects.all().filter(published=True,destination__slug=slug_destination,where_to_go__slug=slug)[:6]
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PackageDestinationOfftheBeatenListApi(APIView):
    def get(self, request, slug):
        packages = Package.objects.all().filter(destination__slug=slug, )
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PackageListApi(APIView):
    def get(self, request):
        packages = Package.objects.all().filter(published=True)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PackageOptionalTours(APIView):
    def get(self, request):
        packages = Package.objects.all().filter(optional=True)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PackageRetrieveApi(APIView):
    def get(self, request, slug):
        package = get_object(slug)
        serializer = PackageDetailSerializer(package)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PackageTypeListApi(APIView):
    def get(self, request):
        types = PackageType.objects.all().filter(active=True)
        serializer = PackageTypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Package Types

class PackageTypeNavApi(APIView):
    def get(self, request):
        packages = PackageType.objects.all().filter(active=True)
        serializer = PackageTypeNavSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PackageTypeHomeApi(APIView):
    def get(self, request):
        packages = PackageType.objects.all().filter(active=True)
        serializer = PackageTypeHomeSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PackageTypeRetrieve(APIView):
    def get(self, request, slug):
        packageType = get_object_package_type(slug)
        serializer = PackageTypeSerializer(packageType)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Interest

class InterestListApi(APIView):
    def get(self, request):
        interests = Interest.objects.all().filter(active=True)
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PackageFilter(filters.FilterSet):

    slug = CharInFilter(field_name="country__slug", lookup_expr="in")

    destination = NumberInFilter(field_name="destination", lookup_expr="in")
    start = filters.NumberFilter(field_name ="days", lookup_expr='gte')
    end = filters.NumberFilter(field_name="days", lookup_expr='lte')
    activity = NumberInFilter(field_name="activity", lookup_expr="in")
    types = NumberInFilter(field_name='package_type__id', lookup_expr="in")
    interests = NumberInFilter(field_name='interest__id', lookup_expr="in")
    months = CharInFilter(field_name='month__name', lookup_expr="in")

    class Meta:
        model = Package
        fields = ['slug', 'destination', 'start', 'end', 'activity', 'types', 'interests', 'months']


class PackageDestinationFilter(filters.FilterSet):

    where_to_go = NumberInFilter(field_name="where_to_go", lookup_expr="in")
    start = filters.NumberFilter(field_name ="days", lookup_expr='gte')
    end = filters.NumberFilter(field_name="days", lookup_expr='lte')
    activity = NumberInFilter(field_name="activity", lookup_expr="in")
    types = NumberInFilter(field_name='package_type__id', lookup_expr="in")
    interests = NumberInFilter(field_name='interest__id', lookup_expr="in")
    months = CharInFilter(field_name='month__name', lookup_expr="in")

    class Meta:
        model = Package
        fields = ['where_to_go', 'start', 'end', 'activity', 'types', 'interests', 'months']

class PackageOptionalFilter(filters.FilterSet):
    destination = NumberInFilter(field_name="destination", lookup_expr="in")

    class Meta:
        model = Package
        fields = ['destination']


class PackageSearchApi(generics.ListAPIView):
    queryset = Package.objects.all().filter(published=True).order_by('-rating').distinct()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageFilter


class PackageDestinationSearchApi(generics.ListAPIView):
    queryset = Package.objects.all().filter(published=True).order_by('-rating').distinct()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageDestinationFilter



class PackageDestinationListApi(generics.ListAPIView):
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageDestinationFilter
    def get_queryset(self):
        return Package.objects.all().filter(published=True,destination__slug=self.kwargs['slug'])
        # return Response(serializer.data, status=status.HTTP_200_OK)

class PackageOptionalSearchApi(generics.ListAPIView):
    queryset = Package.objects.all().filter(optional=True).distinct()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageOptionalFilter

class PackageTitleApi(APIView):
    def get(self, request):
        packages = Package.objects.all().filter(published=True).order_by('-rating')
        serializer = PackageTitleSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)