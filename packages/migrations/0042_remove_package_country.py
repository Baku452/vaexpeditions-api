# Generated by Django 3.2.4 on 2022-04-01 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0041_alter_package_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='country',
        ),
    ]