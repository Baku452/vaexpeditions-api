# Generated by Django 3.1.2 on 2020-11-14 16:55

from django.db import migrations
import imagekit.models.fields
import packages.models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0013_auto_20201114_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='packageimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to=packages.models.path_and_rename_package),
            preserve_default=False,
        ),
    ]
