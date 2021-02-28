from .models import (
    ItineraryOld,
)
from rest_framework import serializers


class ItineraryOldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryOld
        fields = '__all__'
