from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Itinerary
from .serializers import (
    ItinerarySerializer
)

from rest_framework import generics
from django_filters import rest_framework as filters


def get_object(pk):
    try:
        return Itinerary.objects.all().filter(package=pk)#get(pk=pk)
    except Itinerary.DoesNotExist:
        raise Http404


class ItineraryRetrieveApi(APIView):
    def get(self, request, pk):
        itineraries = get_object(pk)
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

