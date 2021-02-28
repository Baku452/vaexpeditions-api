from .models import PopUp
from rest_framework import serializers

class PopUpSerializer(serializers.ModelSerializer):
    original = serializers.ImageField(read_only=True)

    class Meta:
        model = PopUp
        fields = '__all__'