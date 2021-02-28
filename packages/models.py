from django.db import models
from specialists.models import Specialist
from tinymce.models import HTMLField
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField, ProcessedImageField
from autoslug import AutoSlugField
from imagekit.processors import ResizeToFill
from destinations.models import Destination
from django.core.validators import FileExtensionValidator
from smart_selects.db_fields import ChainedForeignKey
import os


RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

ACTIVITY_CHOICES = (
    (1, "Very HIgh"),
    (2, "HIgh"),
    (3, "Moderate"),
    (4, "Low"),
    (5, "Very Low"),
)

DAYS_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
    (21, 21),
    (22, 22),
    (23, 23),
    (24, 24),
    (25, 25),
    (26, 26),
    (27, 27),
    (28, 28),
    (29, 29),
    (30, 30),
    (31, 31),
    (32, 32),
    (33, 33),
    (34, 34),
    (35, 35),
    (36, 36),
    (37, 37),
    (38, 38),
)

MONTHS_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)


def path_and_rename(instance, filename):
    upload_to = 'images/packages-thumbnail/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.slug, ext)
    else:
        filename = '{}.{}'.format(instance.slug, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_package(instance, filename):

    upload_to = 'images/package/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.slug, ext)
    else:
        filename = '{}.{}'.format(instance.slug, ext)
    return os.path.join(upload_to, filename)


class Month(models.Model):
    name = models.CharField(
        unique=True,
        max_length=255,
        choices=MONTHS_CHOICES,
        default=1
    )

    class Meta:
        db_table = 'month'
        ordering = ('id',)

    def __str__(self):
        return self.name


class PackageType(models.Model):
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    svg = models.FileField(
        upload_to='images/package_type/',
        default='',
        validators=[FileExtensionValidator(['svg'])]
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'package_type'
        ordering = ['order']

    def __str__(self):
        return self.title


class Interest(models.Model):
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    package_types = models.ManyToManyField(PackageType)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'interest'
        ordering = ['order']

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')

    package_type = models.ManyToManyField(PackageType)

    image = models.FileField(upload_to='images/experience/')

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(340, 440)],
        format='JPEG',
        options={'quality': 98}
    )

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1500, 800)],
        format='JPEG',
        options={'quality': 98}
    )

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'experience'

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.CharField(max_length=255, default='')

    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title'],
        always_update=True
    )

    content = HTMLField()

    keywords = models.TextField(default='')

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification'

    def __str__(self):
        return self.title


class Package(models.Model):
    title = models.CharField(max_length=255, default='')
    keywords = models.TextField(default='')

    summary = models.TextField(max_length=350, default='')
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title'],
        always_update=True
    )

    description = HTMLField()
    whats_included = HTMLField(default=None, blank=True)
    whats_not_included = HTMLField(default=None, blank=True)

    package_type = models.ManyToManyField(PackageType)

    related_packages = models.ManyToManyField(
        "self",
        blank=True,
        default=None,
    )

    interest = models.ManyToManyField(Interest)

    month = models.ManyToManyField(Month)

    specialist = models.ForeignKey(
        Specialist,
        related_name='specialist',
        default=None,
        on_delete=models.CASCADE,
    )

    destination = models.ForeignKey(
        Destination,
        default=None,
        on_delete=models.CASCADE,
    )

    activity = models.IntegerField(
        choices=ACTIVITY_CHOICES,
        default=1
    )

    days = models.IntegerField(
        choices=DAYS_CHOICES,
        default=1
    )

    physical_difficulty = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default='1'
    )

    cultural_rating = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default='1'
    )

    wildlife_expectation = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default='1'
    )

    thumbnail = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(390, 230)],
        format='JPEG',
        options={'quality': 100},
        blank = True
    )
    old_overview = HTMLField(blank=True)
    published = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    optional = models.BooleanField(default=False)
    show_specialist = models.BooleanField(default=False)
    recommendations = HTMLField(blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'package'

    def __str__(self):
        return self.title


class PackageImage(models.Model):
    package = models.ForeignKey(
        Package,
        related_name='images',
        default=None,
        on_delete=models.CASCADE
    )
    alt = models.CharField(max_length=255, default='')

    slug = AutoSlugField(
        populate_from='alt',
        unique_with=['alt'],
        always_update=True
    )

    image = ProcessedImageField(
        upload_to=path_and_rename_package,
        processors=[ResizeToFill(1600, 700)],
        format='JPEG',
        options={'quality': 100}
    )

    class Meta:
        db_table = 'package_image'

    def __str__(self):
        return self.alt

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % self.image)




