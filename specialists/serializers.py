from .models import ContactUs, Newsletter
from rest_framework import serializers
from packages.models import PackageType


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):

    package_type = serializers.PrimaryKeyRelatedField(
         many=True,
         queryset=PackageType.objects.all()
    )

    class Meta:
        model = Newsletter
        fields = '__all__'
