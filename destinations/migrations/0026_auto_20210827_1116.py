# Generated by Django 3.2.4 on 2021-08-27 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0025_auto_20210827_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wheretogo',
            options={'verbose_name_plural': 'Where to Go - Items'},
        ),
        migrations.RemoveField(
            model_name='wheretogo',
            name='thumbnail',
        ),
    ]
