from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
import os

class PopUp(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')

    image = models.FileField(upload_to='images/popup/', blank=True, null=True)
    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(346, 714)],
        format='JPEG',
        options={'quality': 98},
    )

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'popup'

    def __str__(self):
        return self.title