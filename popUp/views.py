from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import PopUp
from .serializers import (
    PopUpSerializer,
)

from rest_framework import generics
from django_filters import rest_framework as filters

class PopUpListApi(APIView):
    def get(self, request):
        popup = PopUp.objects.all().filter(active=True)
        serializer = PopUpSerializer(popup, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
