# Generated by Django 3.1.4 on 2021-01-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0002_newsletter_package_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='package',
            field=models.CharField(default='', max_length=255),
        ),
    ]
