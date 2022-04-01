# Generated by Django 3.2.4 on 2022-04-01 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0042_auto_20220401_1243'),
        ('packages', '0040_auto_20220317_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='destinations.country'),
        ),
    ]