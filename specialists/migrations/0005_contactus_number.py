# Generated by Django 3.2.4 on 2021-12-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0004_specialist_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='number',
            field=models.CharField(default='', max_length=255),
        ),
    ]
