from .models import Package, PackageType, PackageImage, Experience, Interest, Notification
from specialists.models import Specialist
from rest_framework import serializers
from itineraries.serializers import ItinerarySerializer


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

    class Meta:
        model = Package
        fields = '__all__'


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

    class Meta:
        model = Package
        fields = '__all__'


class PackageDetailTypesSerializer(serializers.ModelSerializer):

    package_type = PackageTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = '__all__'