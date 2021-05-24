# Generated by Django 3.1.4 on 2021-02-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0008_datesandprices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datesandprices',
            name='year',
            field=models.IntegerField(choices=[(2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026'), (2027, '2027'), (2028, '2028'), (2029, '2029')], default=2021),
        ),
    ]
