# Generated by Django 3.2 on 2021-09-28 22:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0003_contactus_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='content',
            field=tinymce.models.HTMLField(default='null'),
            preserve_default=False,
        ),
    ]
