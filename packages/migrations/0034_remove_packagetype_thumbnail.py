# Generated by Django 3.2.4 on 2021-09-21 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0033_packagetype_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagetype',
            name='thumbnail',
        ),
    ]