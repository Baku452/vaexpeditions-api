# Generated by Django 3.1.7 on 2021-05-25 15:39

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0027_auto_20210305_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='old_overview',
        ),
        migrations.RemoveField(
            model_name='package',
            name='related_packages',
        ),
        migrations.AddField(
            model_name='package',
            name='highligths',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='package',
            name='luxury',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='package',
            name='offer',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='package',
            name='promo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='package',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='package',
            name='saveUpTo',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='package',
            name='titleSEO',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='package',
            name='activity',
            field=models.IntegerField(choices=[(1, 'Very High'), (2, 'High'), (3, 'Moderate'), (4, 'Low'), (5, 'Very Low')], default=1),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/package-type/'),
        ),
    ]
