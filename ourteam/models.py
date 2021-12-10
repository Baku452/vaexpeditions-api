from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField, ProcessedImageField
from autoslug import AutoSlugField
from tinymce.models import HTMLField

# Create your models here.


class Collaborator(models.Model):
    name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    job = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    hobbies = HTMLField(default="")
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    slug = AutoSlugField(
        populate_from="full_name",
        unique_with=["name"],
        always_update=True,
    )
    image = models.FileField(upload_to="images/ourteam/", blank=False, null=True)
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 420)],
        format="JPEG",
        options={"quality": 90},
    )

    class Meta:
        db_table = "collaborators"
        ordering = ["order"]

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

    def __str__(self):
        return self.name
