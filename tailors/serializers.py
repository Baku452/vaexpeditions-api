from .models import Tailor
from rest_framework import serializers

class TailorSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Tailor
        fields = '__all__'
