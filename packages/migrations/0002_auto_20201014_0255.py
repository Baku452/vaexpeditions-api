# Generated by Django 3.1.1 on 2020-10-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='keywords',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='package',
            name='summary',
            field=models.TextField(default='', max_length=350),
        ),
    ]
