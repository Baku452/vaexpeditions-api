from django.db import models
from tinymce.models import HTMLField
from packages.models import Package
from autoslug import AutoSlugField
import os

class ItineraryOld(models.Model):

    package = models.ForeignKey(
        Package,
        default=None,
        related_name='old_itinerario',
        on_delete=models.CASCADE
    )

    subtitle = models.CharField(max_length=255, default='')
    content = HTMLField()

    limit = models.PositiveIntegerField(default=0, blank=False, null=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'old_itinerario'
        ordering = ['order']

    def __str__(self):
        return self.subtitle