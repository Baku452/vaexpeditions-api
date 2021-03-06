# Generated by Django 3.2.4 on 2021-08-27 16:05

import autoslug.fields
import destinations.models
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0024_wheretogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='wheretogo',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default='null', editable=False, populate_from='title', unique_with=['title']),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wheretogo',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='null', upload_to=destinations.models.path_and_rename_where),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wheretogo',
            name='image',
            field=models.FileField(upload_to='images/whereto/'),
        ),
        migrations.CreateModel(
            name='ItemWhere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, default='', max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('WhereToGo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='destinations.wheretogo')),
            ],
            options={
                'db_table': 'itemwheretogo',
            },
        ),
    ]
