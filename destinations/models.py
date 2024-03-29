from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
import os


def path_and_rename(instance, filename):
    upload_to = "images/banner/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.slug, ext)
    else:
        filename = "{}.{}".format(instance.slug, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_destination(instance, filename):
    upload_to = "images/destination/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.slug, ext)
    else:
        filename = "{}.{}".format(instance.slug, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_where(instance, filename):
    upload_to = "images/whereto/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.slug, ext)
    else:
        filename = "{}.{}".format(instance.slug, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_continent(instance, filename):
    upload_to = "images/continent/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.slug, ext)
    else:
        filename = "{}.{}".format(instance.slug, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_itemWhere(instance, filename):
    upload_to = "images/whereto/items"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.title, ext)
    else:
        filename = "{}.{}".format(instance.title, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_travelAdvice(instance, filename):
    upload_to = "images/destination/traveladvice/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.title, ext)
    else:
        filename = "{}.{}".format(instance.title, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_subDestination(instance, filename):
    upload_to = "images/destination/sub-destination/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.title, ext)
    else:
        filename = "{}.{}".format(instance.title, ext)
    return os.path.join(upload_to, filename)


MONTHS_CHOICES = (
    ("JAN", "January"),
    ("FEB", "February"),
    ("MAR", "March"),
    ("APR", "April"),
    ("MAY", "May"),
    ("JUN", "June"),
    ("JUL", "July"),
    ("AUG", "August"),
    ("SEP", "September"),
    ("OCT", "October"),
    ("NOV", "November"),
    ("DEC", "December"),
)

class Continent(models.Model):
    name = models.CharField(max_length=255)
    content = HTMLField(default=None, blank=True, null=True)
    quote = HTMLField(default=None, blank=True, null=True)
    slug = AutoSlugField(populate_from="name", unique_with=["name"], always_update=True)
    image = models.FileField(upload_to="images/countries/")
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(350, 250)],
        format="JPEG",
        options={"quality": 98},
    )
    original = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1600, 700)],
        format="JPEG",
        options={"quality": 98},
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "continent"
        ordering = ["order"]
        verbose_name_plural = "Continents"

    def __str__(self):
        return self.name


class ContinentImage(models.Model):
    continent = models.ForeignKey(Continent, related_name="images", default=None, null=True, on_delete=models.CASCADE)
    alt = models.CharField(max_length=255, default="")
    slug = AutoSlugField(populate_from="alt", unique_with=["alt"], always_update=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = ProcessedImageField(
        upload_to=path_and_rename_continent,
        processors=[ResizeToFill(1600, 700)],
        format="JPEG",
        options={"quality": 100},
    )

    class Meta:
        db_table = "continent_image"
        ordering = ["order"]

    def __str__(self):
        return self.alt

    def image_tag(self):
        return mark_safe(
            '<img src="/media/%s" width="150" height="150" />' % self.image
        )


class Destination(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, default="", blank=True)
    summary = models.TextField(max_length=150, default="", blank=True)
    slug = AutoSlugField(
        populate_from="title", unique_with=["title"], always_update=True
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = models.FileField(upload_to="images/countries/")
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(350, 200)],
        format="JPEG",
        options={"quality": 98},
    )
    image_home = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1200, 515)],
        format="JPEG",
        options={"quality": 90},
    )
    original = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1600, 700)],
        format="JPEG",
        options={"quality": 98},
    )
    content = HTMLField(default=None, blank=True, null=True)
    travelfact = HTMLField(default=None, blank=True, null=True)
    travelAdvice = RichTextUploadingField()
    bestTime = HTMLField(default=None, blank=True, null=True)
    imageTraveFact = models.FileField(upload_to="images/countries/")
    weather_content = HTMLField(default=None, blank=True, null=True)
    continent = models.ForeignKey(
        Continent, default=None, null=True, related_name="destinations", on_delete=models.CASCADE
    )
    tailor_made = models.BooleanField(default=False)
    is_what_to_do = models.BooleanField(default=False)
    is_why_reason = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "destination"
        ordering = ["order"]
        verbose_name_plural = "Destinations - Countries"

    def __str__(self):
        return self.title


class Reason(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=150, default="", blank=True)
    destination = models.ForeignKey(
        Destination, default=None, related_name="reasons", on_delete=models.CASCADE
    )
    image = models.FileField(upload_to="images/reasons/")
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(390, 230)],
        format="JPEG",
        options={"quality": 98},
    )
    original = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1600, 700)],
        format="JPEG",
        options={"quality": 98},
    )
    interest = models.ForeignKey(
        to="packages.Interest",
        default=None,
        blank=True,
        null=True,
        related_name="interests",
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reason"

    def __str__(self):
        return self.title


class DestinationImage(models.Model):
    destination = models.ForeignKey(
        Destination, related_name="images", default=None, on_delete=models.CASCADE
    )
    alt = models.CharField(max_length=255, default="")
    slug = AutoSlugField(populate_from="alt", unique_with=["alt"], always_update=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = ProcessedImageField(
        upload_to=path_and_rename_destination, format="JPEG", options={"quality": 100}
    )

    class Meta:
        db_table = "destination_image"
        ordering = ["order"]

    def image_tag(self):
        return mark_safe(
            '<img src="/media/%s" width="150" height="150" />' % self.image
        )


class WeatherItems(models.Model):
    month = models.CharField(max_length=100, choices=MONTHS_CHOICES, default="")
    destination = models.ForeignKey(
        Destination, default=None, related_name="weathers", on_delete=models.CASCADE
    )
    degrees = models.IntegerField(default=0, blank=False, null=False)
    rain = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = "weather_items"

    def __str__(self):
        return self.month


class Banner(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, default="")
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    slug = AutoSlugField(populate_from="name", unique_with=["name"], always_update=True)

    image = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(1600, 700)],
        format="JPEG",
        options={"quality": 100},
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "banner"
        ordering = ["order"]

    def __str__(self):
        return self.name


class FaqDest(models.Model):

    destination = models.ForeignKey(
        Destination, default=None, related_name="faqs", on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255, default="")
    content = HTMLField()
    active = models.BooleanField(default=True)
    preTravel = models.BooleanField(default=False)
    onTravel = models.BooleanField(default=False)
    postTravel = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "faqDest"
        ordering = ["order"]

    def __str__(self):
        return self.title


class WhereToGo(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=150, default="", blank=True)
    content = HTMLField()
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    Destination = models.ForeignKey(
        Destination, default=None, related_name="where", on_delete=models.CASCADE
    )
    image = models.FileField(upload_to="images/whereto/")
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(385, 290)],
        format="JPEG",
        options={"quality": 100},
    )
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wheretogo"
        verbose_name_plural = "Where to Go - Items"

    def __str__(self):
        return self.title

class HighLigths(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=150, default="", blank=True)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    Destination = models.ForeignKey(
        Destination, default=None, related_name="highligths", on_delete=models.CASCADE
    )
    image = models.FileField(upload_to="images/highligths/")
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(385, 290)],
        format="JPEG",
        options={"quality": 100},
    )
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "highligths"
        verbose_name_plural = "highligths"

    def __str__(self):
        return self.title


class ItemWhere(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    image = ProcessedImageField(
        upload_to=path_and_rename_itemWhere,
        processors=[ResizeToFill(390, 230)],
        format="JPEG",
        options={"quality": 100},
    )

    WhereToGo = models.ForeignKey(
        WhereToGo, default=None, related_name="items", on_delete=models.CASCADE
    )
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "itemwheretogo"

    def __str__(self):
        return self.title


class TravelAdvice(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    image = ProcessedImageField(
        upload_to=path_and_rename_travelAdvice,
        processors=[ResizeToFill(350, 430)],
        format="JPEG",
        options={"quality": 100},
    )

    destination = models.ForeignKey(
        Destination, default=None, related_name="advice", on_delete=models.CASCADE
    )
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "traveladvice"

    def __str__(self):
        return self.title
