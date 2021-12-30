from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

# Create your views here.
from .models import Blog, BlogType, Destination, Blogger

from .serializers import (
    BlogDetailSerializer,
    BlogTypeSerializer,
    BlogDetailTypesSerializer,
    BlogSerializer,
    BloggerSerializer,

)

from rest_framework import generics
from django_filters import rest_framework as filters

def get_object(slug):
    try:
        return Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        raise Http404

def get_object_id(user):
    try:
        return Blogger.objects.get(user=user)
    except Blogger.DoesNotExist:
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
    types = NumberInFilter(field_name="blog_type__id", lookup_expr="in")
    interest = NumberInFilter(field_name="interest__id", lookup_expr="in")

    class Meta:
        model = Blog
        fields = ["destination", "types", "interest"]


class BlogSearchApi(generics.ListAPIView):
    queryset = Blog.objects.all().filter(published=True).order_by("-created").distinct()
    serializer_class = BlogDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter


class BlogListApi(generics.ListAPIView):
    queryset = (
        Blog.objects.all().filter(published=True).order_by("-created").distinct()[:4]
    )
    serializer_class = BlogSerializer

class BloggerRetrieveApi(APIView):
    def get(self, request, user):
        blogger = get_object_id(user)
        serializer = BloggerSerializer(blogger)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BloggerListApi(generics.ListAPIView):
    queryset = Blogger.objects.all().distinct()
    serializer_class = BloggerSerializer

class BlogPopular(generics.ListAPIView):
    queryset = (
        Blog.objects.all()
        .filter(published=True, popular=True)
        .order_by("-created")
        .distinct()
    )
    serializer_class = BlogDetailSerializer
