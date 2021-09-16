from .models import Package, PackageType, PackageImage, Experience, Interest, Notification
from specialists.models import Specialist
from rest_framework import serializers
from itineraries.serializers import (
    ItinerarySerializer,
    FaqSerializer,
    DatesAndPricesSerializer,
)


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    type_name = serializers.StringRelatedField(many=True, source="package_type")
    destination_name = serializers.StringRelatedField(source="destination")
    activity_name = serializers.StringRelatedField(source="activity")
    class Meta:
        model = Package
        fields = ['id','title','slug','activity','days','published','destination','package_type','interest','destination_name','thumbnail','type_name','activity_name','summary']

class PackageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['title','slug','days', 'package_type']

class PackageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageType
        fields = '__all__'


class PackageImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageImage
        fields = ['id', 'image', 'alt']


class SpecialistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialist
        fields = '__all__'


class PackageDetailSerializer(serializers.ModelSerializer):

    images = PackageImageSerializer(many=True, read_only=True)
    specialist = SpecialistSerializer()
    itineraries = ItinerarySerializer(many=True, read_only=True)
    related_packages = PackageSerializer(many=True, read_only=True)
    faqs = FaqSerializer(many=True, read_only=True)
    dates_prices = DatesAndPricesSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = '__all__'


class PackageDetailTypesSerializer(serializers.ModelSerializer):

    package_type = PackageTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = '__all__'