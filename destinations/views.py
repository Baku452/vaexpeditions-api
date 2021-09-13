from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.http import Http404

from .models import Destination, Country, Banner, WhereToGo
from .serializers import CountrySerializer, BannerSerializer, DestinationSerializer, CitySerializer, WhereSerializer, DestinationHomeSerializer


def get_object(slug):
    try:
        return Destination.objects.get(slug=slug)
    except Destination.DoesNotExist:
        raise Http404


def get_object_country(slug):
    try:
        return Country.objects.get(slug=slug)
    except Country.DoesNotExist:
        raise Http404

def get_object_city(slug):
    try:
        return WhereToGo.objects.get(slug=slug)
    except WhereToGo.DoesNotExist:
        raise Http404


class CountryRetrieveApi(APIView):
    def get(self, request, slug):
        country = get_object_country(slug)
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=HTTP_200_OK)


class CountryListApi(APIView):
    def get(self, request):
        countries = Country.objects.filter(active=True)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class DestinationRetrieveApi(APIView):
    def get(self, request, slug):
        destination = get_object(slug)
        serializer = DestinationSerializer(destination)
        return Response(serializer.data, status=HTTP_200_OK)


class EveryoneDestinationApi(APIView):
    def get(self, request):
        destinations = Destination.objects.filter(active=True)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class DestinationListApi(APIView):
    def get(self, request):
        countries = Country.objects.filter(active=True)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class DestinationTitleBannerApi(APIView):
    def get(self, request):
        destinations = Destination.objects.filter(active=True)
        serializer = DestinationHomeSerializer(destinations, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class BannerListApi(APIView):
    def get(self, request):
        banners = Banner.objects.all().filter(active=True)
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class CitiesApi(APIView):
    def get(self, request):
        cities = WhereToGo.objects.all().filter(active=True)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class CityRetrieveApi(APIView):
    def get(self, request, slug, slug_destination):
        city = get_object_city(slug)
        serializer = CitySerializer(city)
        return Response(serializer.data, status=HTTP_200_OK)
