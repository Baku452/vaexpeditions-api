from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
import os


def path_and_rename(instance, filename):
    upload_to = 'images/banner/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.slug, ext)
    else:
        filename = '{}.{}'.format(instance.slug, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_destination(instance, filename):
    upload_to = 'images/destination/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.slug, ext)
    else:
        filename = '{}.{}'.format(instance.slug, ext)
    return os.path.join(upload_to, filename)


class Country(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Destination(models.Model):
    title = models.CharField(max_length=255)

    sub_title = models.CharField(
        max_length=255,
        default='',
        blank=True

    )

    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title'],
        always_update=True
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    picture = ProcessedImageField(
        upload_to=path_and_rename_destination,
        processors=[ResizeToFill(1600, 700)],
        format='JPEG',
        options={'quality': 100}
    )

    content = HTMLField()

    country = models.ForeignKey(
        Country,
        default=None,
        related_name='destinations',
        on_delete=models.CASCADE
    )

    tailor_made = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'destination'
        ordering = ['order']

    def __str__(self):
        return self.title


class Banner(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, default="")
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    slug = AutoSlugField(
        populate_from='name',
        unique_with=['name'],
        always_update=True
    )

    image = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(1600, 700)],
        format='JPEG',
        options={'quality': 100}
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banner'
        ordering = ['order']

    def __str__(self):
        return self.name
