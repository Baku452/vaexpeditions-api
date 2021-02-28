from .models import History
from rest_framework import serializers

class HistorySerializer(serializers.ModelSerializer):
    original = serializers.ImageField(read_only=True)

    class Meta:
        model = History
        fields = '__all__'