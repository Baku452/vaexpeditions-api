# Generated by Django 3.2.4 on 2021-08-24 19:36

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0016_auto_20210305_0441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['order'], 'verbose_name_plural': 'Continents'},
        ),
        migrations.AlterModelOptions(
            name='destination',
            options={'ordering': ['order'], 'verbose_name_plural': 'Destinations - Countries'},
        ),
        migrations.CreateModel(
            name='FaqDest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('destination', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='destinations.destination')),
            ],
            options={
                'db_table': 'faqDest',
                'ordering': ['order'],
            },
        ),
    ]
