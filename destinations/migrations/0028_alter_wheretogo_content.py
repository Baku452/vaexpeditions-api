# Generated by Django 3.2.4 on 2021-08-27 16:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0027_wheretogo_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wheretogo',
            name='content',
            field=tinymce.models.HTMLField(default='null'),
            preserve_default=False,
        ),
    ]
