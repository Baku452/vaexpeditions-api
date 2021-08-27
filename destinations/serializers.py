from .models import Country, Banner, Destination, Reason, WeatherItems, FaqDest, DestinationImage, ContinentImage, WhereToGo
from packages.models import Package
from rest_framework import serializers
from packages.serializers import PackageTypeSerializer, PackageSerializer


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

class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqDest
        fields = '__all__'

class WhereSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    class Meta:
        model = WhereToGo
        fields = '__all__'

class DestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = '__all__' 

class PackageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    type_name = serializers.StringRelatedField(many=True, source="package_type")
    activity_name = serializers.StringRelatedField(source="activity")
    class Meta:
        model = Package
        fields = ['id','title','days','slug','type_name','summary','thumbnail','activity_name']

class ContinentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = '__all__' 


class DestinationSerializer(serializers.ModelSerializer):
    reasons = ReasonSerializer(many=True, read_only=True)
    packages = PackageSerializer(many=True, read_only=True)
    faqs = FAQsSerializer(many=True, read_only=True)
    images = DestImageSerializer(many=True, read_only=True)
    weathers = WeatherItemsSerializer(many=True, read_only=True)
    where = WhereSerializer(many=True, read_only=True)
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
    images = ContinentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

