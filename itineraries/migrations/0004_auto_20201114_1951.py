# Generated by Django 3.1.2 on 2020-11-14 19:51

import autoslug.fields
from django.db import migrations
import imagekit.models.fields
import itineraries.models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0003_auto_20201114_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='itineraryimage',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default='', editable=False, populate_from='alt', unique_with=['alt']),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itineraryimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=itineraries.models.path_and_rename),
        ),
    ]
