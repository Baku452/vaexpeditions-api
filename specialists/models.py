from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Specialist(models.Model):
    fullname = models.CharField(max_length=255, default="")
    content = HTMLField()
    email = models.EmailField(max_length=255, default="")
    calendly = models.CharField(max_length=255, default="", blank = True, null = True)
    thumbnail = ProcessedImageField(
        upload_to="specialist-thumbnail",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 100},
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "specialist"

    def __str__(self):
        return self.fullname


class Newsletter(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")

    package_type = models.ManyToManyField(to="packages.PackageType")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "newsletter"

    def __str__(self):
        return self.first_name


class ContactUs(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")
    destination_interest = models.CharField(max_length=255, default="")
    package = models.CharField(max_length=255, default="", blank = True, null = True)
    phone = models.CharField(max_length=255, default="")
    message = models.TextField(max_length=999, default="")
    typeClient = models.TextField(max_length=255, default="")
    company = models.TextField(max_length=255, default="")
    is_newsletter = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "contact_us"

    def __str__(self):
        return self.first_name


class ContactUsB2C(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    package = models.CharField(max_length=255, default="")
    message = models.TextField(max_length=999, default="")
    extra_data = models.TextField(max_length=999, default="")
    typeClient = models.TextField(max_length=255, default="")
    company = models.TextField(max_length=255, default="")
    is_newsletter = models.BooleanField(default=False)
    is_promo = models.BooleanField(default=False)
    url = models.CharField(max_length=255, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "contact_usB2C"

    def __str__(self):
        return self.first_name
