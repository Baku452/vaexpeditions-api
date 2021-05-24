from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
import os

class Tailor(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')

    image = models.FileField(upload_to='images/tailors/', blank=True, null=True)

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(545, 276)],
        format='JPEG',
        options={'quality': 98},
    )

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1500, 800)],
        format='JPEG',
        options={'quality': 98},
    )

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tailor'

    def __str__(self):
        return self.title