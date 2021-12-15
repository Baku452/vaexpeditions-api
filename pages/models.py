import os

from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255, default="")
    keywords = models.TextField(default="")
    titleSEO = models.TextField(max_length=255, default="", blank=True)
    content = RichTextUploadingField()
    slug = AutoSlugField(
        populate_from="title", unique_with=["title"], always_update=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "page"

    def __str__(self):
        return self.title

    @property
    def URL(self):
        return os.getenv("NEXTJS_DOMAIN") + "/%s" % (self.slug)
