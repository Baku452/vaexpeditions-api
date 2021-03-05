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


class Country(models.Model):
    name = models.CharField(max_length=255)
    content = HTMLField(default=None, blank=True, null=True)

    slug = AutoSlugField(
        populate_from='name',
        unique_with=['name'],
        always_update=True
    )

    image = models.FileField(upload_to='images/countries/')

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(350, 250)],
        format='JPEG',
        options={'quality': 98}
    )

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1600, 700)],
        format='JPEG',
        options={'quality': 98}
    )

    package_type = models.ManyToManyField(to='packages.PackageType')

    show_tab_overview = models.BooleanField(default=True)
    show_tab_holidays = models.BooleanField(default=True)
    show_tab_tour_in = models.BooleanField(default=True)
    show_tab_reason_why = models.BooleanField(default=True)
    show_tab_what_to_do = models.BooleanField(default=True)
    show_tab_when_to_go = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        ordering = ['order']
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

    summary = models.TextField(max_length=150, default='', blank=True)

    #reasons = models.ManyToManyField(Reason)

    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title'],
        always_update=True
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    image = models.FileField(upload_to='images/countries/')

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(350, 200)],
        format='JPEG',
        options={'quality': 98}
    )

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1600, 700)],
        format='JPEG',
        options={'quality': 98}
    )

    content = HTMLField(default=None, blank=True, null=True)

    weather_content = HTMLField(default=None, blank=True, null=True)

    country = models.ForeignKey(
        Country,
        default=None,
        related_name='destinations',
        on_delete=models.CASCADE
    )

    tailor_made = models.BooleanField(default=False)

    is_what_to_do = models.BooleanField(default=False)
    is_why_reason = models.BooleanField(default=False)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'destination'
        ordering = ['order']

    def __str__(self):
        return self.title


class Reason(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=150, default='', blank=True)

    destination = models.ForeignKey(
        Destination,
        default=None,
        related_name='reasons',
        on_delete=models.CASCADE
    )

    image = models.FileField(upload_to='images/reasons/')

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(390, 230)],
        format='JPEG',
        options={'quality': 98}
    )

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1600, 700)],
        format='JPEG',
        options={'quality': 98}
    )

    interest = models.ForeignKey(
        to='packages.Interest',
        default=None,
        blank=True,
        null=True,
        related_name='interests',
        on_delete=models.CASCADE
    )

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reason'

    def __str__(self):
        return self.title


class WeatherItems(models.Model):

    month = models.CharField(
        max_length=100,
        choices=MONTHS_CHOICES,
        default=''
    )

    destination = models.ForeignKey(
        Destination,
        default=None,
        related_name='weathers',
        on_delete=models.CASCADE
    )

    degrees = models.IntegerField(default=0, blank=False, null=False)
    rain = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = 'weather_items'

    def __str__(self):
        return self.month


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
