# Generated by Django 3.2.4 on 2021-09-16 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0034_alter_destination_traveladvice'),
        ('packages', '0029_packageimage_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packageimage',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='package',
            name='days',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38)], default=1),
        ),
        migrations.AlterField(
            model_name='package',
            name='destination',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='destinations.destination'),
        ),
        migrations.AlterField(
            model_name='package',
            name='titleSEO',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
    ]
