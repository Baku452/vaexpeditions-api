from rest_framework import serializers
from .models import Collaborator


class CollaboratorSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Collaborator
        fields = "__all__"
