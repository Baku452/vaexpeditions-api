from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Destination, Package, PackageType, Experience, Interest, Notification
from .serializers import (
    PackageSerializer,
    PackageTypeSerializer,
    PackageDetailSerializer,
    ExperienceSerializer,
    PackageDetailTypesSerializer,
    InterestSerializer,
    NotificationSerializer,
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


class PackageRetrieveApi(APIView):
    def get(self, request, slug):
        package = get_object(slug)
        serializer = PackageDetailSerializer(package)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


class PackageTypeListApi(APIView):
    def get(self, request):
        packages = PackageType.objects.all().filter(active=True)
        serializer = PackageTypeSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PackageTypeDetailApi(APIView):
    def get(self, request, pk):
        package = get_object_id(pk)
        serializer = PackageDetailTypesSerializer(package)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterestListApi(APIView):
    def get(self, request):
        interests = Interest.objects.all().filter(active=True)
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PackageHomeListApi(APIView):
    def get(self, request):
        packages = Package.objects.all().filter(published=True, is_home=True)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExperienceListApi(APIView):
    def get(self, request):
        experiences = Experience.objects.all().filter(active=True)
        serializer = ExperienceSerializer(experiences, many=True)
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


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PackageFilter(filters.FilterSet):
    destination = NumberInFilter(field_name="destination", lookup_expr="in")
    start = filters.NumberFilter(field_name ="days", lookup_expr='gte')
    end = filters.NumberFilter(field_name="days", lookup_expr='lte')
    activity = NumberInFilter(field_name="activity", lookup_expr="in")
    types = NumberInFilter(field_name='package_type__id', lookup_expr="in")
    interests = NumberInFilter(field_name='interest__id', lookup_expr="in")
    months = CharInFilter(field_name='month__name', lookup_expr="in")

    class Meta:
        model = Package
        fields = ['destination', 'start', 'end', 'activity', 'types', 'interests', 'months']

class PackageOptionalFilter(filters.FilterSet):
    destination = NumberInFilter(field_name="destination", lookup_expr="in")

    class Meta:
        model = Package
        fields = ['destination']


class PackageSearchApi(generics.ListAPIView):
    queryset = Package.objects.all().filter(published=True).distinct()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageFilter

class PackageOptionalSearchApi(generics.ListAPIView):
    queryset = Package.objects.all().filter(optional=True).distinct()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageOptionalFilter
