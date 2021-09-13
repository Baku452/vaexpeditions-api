# Generated by Django 3.2.4 on 2021-08-27 23:11

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0029_alter_itemwhere_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='bestTime',
            field=tinymce.models.HTMLField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='travelAdvice',
            field=tinymce.models.HTMLField(blank=True, default=None, null=True),
        ),
    ]