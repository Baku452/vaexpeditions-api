# Generated by Django 3.1.4 on 2020-12-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0006_auto_20201114_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='sub_title',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]