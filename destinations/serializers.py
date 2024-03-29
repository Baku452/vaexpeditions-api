from .models import (
    Continent,
    Banner,
    Destination,
    Reason,
    WeatherItems,
    FaqDest,
    DestinationImage,
    ContinentImage,
    WhereToGo,
    ItemWhere,
    TravelAdvice,
    HighLigths
)
from packages.models import Package
from rest_framework import serializers
from packages.serializers import PackageTypeSerializer, PackageSerializer


class WeatherItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherItems
        fields = "__all__"


class ReasonSerializer(serializers.ModelSerializer):

    thumbnail = serializers.ImageField(read_only=True)
    original = serializers.ImageField(read_only=True)

    class Meta:
        model = Reason
        fields = "__all__"


class ReasonHomeSerializer(serializers.ModelSerializer):

    thumbnail = serializers.ImageField(read_only=True)
    original = serializers.ImageField(read_only=True)

    class Meta:
        model = Reason
        fields = "__all__"


class FAQsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqDest
        fields = "__all__"


class TravelAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAdvice
        fields = "__all__"


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemWhere
        fields = "__all__"


class WhereSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = WhereToGo
        fields = "__all__"

class HighLigthsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HighLigths
        fields = "__all__"


class WhereHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhereToGo
        fields = ["id", "title", "slug"]


class DestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = "__all__"


class PackageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    type_name = serializers.StringRelatedField(many=True, source="package_type")
    activity_name = serializers.StringRelatedField(source="activity")

    class Meta:
        model = Package
        fields = [
            "id",
            "title",
            "days",
            "slug",
            "type_name",
            "summary",
            "thumbnail",
            "activity_name",
        ]


#Destination Serializer

class DestinationSerializer(serializers.ModelSerializer):
    reasons = ReasonSerializer(many=True, read_only=True)
    packages = PackageSerializer(many=True, read_only=True)
    faqs = FAQsSerializer(many=True, read_only=True)
    advice = TravelAdviceSerializer(many=True, read_only=True)
    images = DestImageSerializer(many=True, read_only=True)
    weathers = WeatherItemsSerializer(many=True, read_only=True)
    where = WhereSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    original = serializers.ImageField(read_only=True)
    highligths = HighLigthsSerializer(many=True,read_only=True )
    destination_name = serializers.StringRelatedField(source="destination")

    class Meta:
        model = Destination
        fields = "__all__"


class DestinationHomeSerializer(serializers.ModelSerializer):
    where = WhereHomeSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    image_home = serializers.ImageField(read_only=True)

    class Meta:
        model = Destination
        fields = [
            "id",
            "title",
            "summary",
            "sub_title",
            "image",
            "thumbnail",
            "slug",
            "where",
            "image_home",
        ]

#Continent Serializer

class ContinentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = "__all__"


class ContinentSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    original = serializers.ImageField(read_only=True)
    images = ContinentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Continent
        fields = "__all__"


class ContinentHomeSerializer(serializers.ModelSerializer):
    destinations = DestinationHomeSerializer(many=True, read_only=True)

    class Meta:
        model = Continent
        fields = ["id", "name", "slug", "destinations"]




#Banner Serializer

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

#City Serializer

class CitySerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    items = ItemsSerializer(many=True, read_only=True)
    slug_destination = serializers.CharField(source="Destination.slug")

    class Meta:
        model = WhereToGo
        fields = "__all__"
