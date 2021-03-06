# Generated by Django 3.2.4 on 2021-08-25 15:47

import autoslug.fields
import destinations.models
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0017_auto_20210824_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(default='', max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='alt', unique_with=['alt'])),
                ('order', models.PositiveIntegerField(default=0)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=destinations.models.path_and_rename_destination)),
                ('destination', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='destinations.destination')),
            ],
            options={
                'db_table': 'destination_image',
                'ordering': ['order'],
            },
        ),
    ]
