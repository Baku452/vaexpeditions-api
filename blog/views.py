from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
# Create your views here.
from .models import Blog, BlogType, Destination

from .serializers import (
   BlogDetailSerializer,
   BlogTypeSerializer,
   BlogDetailTypesSerializer,
   BlogSerializer
)

from rest_framework import generics
from django_filters import rest_framework as filters

def get_object(slug):
    try:
        return Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        raise Http404

class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class BlogRetrieveApi(APIView):
    def get(self, request, slug):
        blog = get_object(slug)
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogTypeListApi(APIView):
    def get(self, request):
        blogs = BlogType.objects.all().filter(active=True)
        serializer = BlogTypeSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogFilter(filters.FilterSet):
    destination = NumberInFilter(field_name="destination", lookup_expr="in")
    types = NumberInFilter(field_name='blog_type__id', lookup_expr="in")

    class Meta:
        model = Blog
        fields = ['destination', 'types']

class BlogSearchApi(generics.ListAPIView):
    queryset = Blog.objects.all().filter(published=True).distinct()
    serializer_class = BlogDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter

class BlogListApi(generics.ListAPIView):
    queryset = Blog.objects.all().filter(published=True).order_by('-created').distinct()[:4]
    serializer_class = BlogSerializer