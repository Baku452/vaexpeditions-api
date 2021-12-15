from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PageSerializer
from .models import Page
from rest_framework import generics
from django.http import Http404
from rest_framework import status

# Create your views here.


def get_object(slug):
    try:
        return Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        raise Http404


class PageApi(APIView):
    def get(self, request, slug):
        page = get_object(slug)
        serializer = PageSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PageListApi(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
