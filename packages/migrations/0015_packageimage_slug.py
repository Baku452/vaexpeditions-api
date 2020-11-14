# Generated by Django 3.1.2 on 2020-11-14 16:56

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0014_packageimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='packageimage',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default='', editable=False, populate_from='alt', unique_with=['alt']),
            preserve_default=False,
        ),
    ]
