from django.shortcuts import render
from rest_framework.response import Response
from .models import Collaborator
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CollaboratorSerializer

# Create your views here.


class CollaboratorRetrieveApi(APIView):
    def get(self, request, slug):
        collaborator = Collaborator.objects.get(slug=slug)
        serializer = CollaboratorSerializer(collaborator)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CollaboratorsListApi(APIView):
    def get(self, request):
        collaborators = Collaborator.objects.all()
        serializer = CollaboratorSerializer(collaborators, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
