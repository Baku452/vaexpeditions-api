from .models import Country, Banner, Destination, Reason, WeatherItems
from rest_framework import serializers
from packages.serializers import PackageTypeSerializer


class WeatherItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherItems
        fields = '__all__'


class ReasonSerializer(serializers.ModelSerializer):

    thumbnail = serializers.ImageField(read_only=True)
    original = serializers.ImageField(read_only=True)

    class Meta:
        model = Reason
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    reasons = ReasonSerializer(many=True, read_only=True)
    weathers = WeatherItemsSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    original = serializers.ImageField(read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    package_type = PackageTypeSerializer(many=True, read_only=True)
    destinations = DestinationSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    original = serializers.ImageField(read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

