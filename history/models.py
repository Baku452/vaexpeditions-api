from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
import os

class History(models.Model):
    title = models.CharField(max_length=255)
    content1 = HTMLField(default='')
    content2 = HTMLField(default='', blank=True)
    image = models.FileField(upload_to='images/history/', blank=True, null=True)

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(638, 425)],
        format='JPEG',
        options={'quality': 98},
    )

    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'history'
        ordering = ['order']

    def __str__(self):
        return self.title