# Generated by Django 3.1.7 on 2021-03-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0012_auto_20210302_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True, default='', max_length=150)),
                ('image', models.FileField(upload_to='images/reasons/')),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'reason',
            },
        ),
        migrations.AddField(
            model_name='destination',
            name='reasons',
            field=models.ManyToManyField(to='destinations.Reason'),
        ),
    ]
