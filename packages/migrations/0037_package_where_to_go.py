# Generated by Django 3.2.4 on 2021-09-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0037_delete_subdestination'),
        ('packages', '0036_auto_20210922_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='where_to_go',
            field=models.ManyToManyField(to='destinations.WhereToGo'),
        ),
    ]