# Generated by Django 3.2.4 on 2021-09-13 09:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0032_alter_destination_travelfact'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='imageTraveFact',
            field=models.FileField(default='null', upload_to='images/countries/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destination',
            name='travelfact',
            field=tinymce.models.HTMLField(blank=True, default=None, null=True),
        ),
    ]
