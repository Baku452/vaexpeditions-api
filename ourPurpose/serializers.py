from .models import OurPurpose
from rest_framework import serializers

class OurPurposeSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = OurPurpose
        fields = '__all__'