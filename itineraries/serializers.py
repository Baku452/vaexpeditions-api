from .models import (
    Itinerary,
    ItineraryImage,
    ItineraryItems,
    Faq,
    DatesAndPrices,
)
from rest_framework import serializers


class ItineraryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItineraryImage
        fields = '__all__'


class ItineraryItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItineraryItems
        fields = '__all__'


class ItinerarySerializer(serializers.ModelSerializer):
    images = ItineraryImageSerializer(many=True, read_only=True)
    items = ItineraryItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = '__all__'

class DatesAndPricesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatesAndPrices
        fields = '__all__'
