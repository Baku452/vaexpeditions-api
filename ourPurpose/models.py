from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
import os

class OurPurpose(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')

    image = models.FileField(upload_to='images/ourPurpose/', blank=True, null=True)

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(432, 342)],
        format='JPEG',
        options={'quality': 98},
    )

    slug = AutoSlugField(
        populate_from = 'title',
        unique_with=['title'],
        always_update=True,
        default=""
    )

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(432, 342)],
        format='JPEG',
        options={'quality': 98},
    )

    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ourpurpose'
        ordering = ['order']

    def __str__(self):
        return self.title