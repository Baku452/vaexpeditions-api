# Generated by Django 3.1.2 on 2020-10-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_remove_package_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'interest',
            },
        ),
        migrations.AddField(
            model_name='packagetype',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='package',
            name='interest',
            field=models.ManyToManyField(to='packages.Interest'),
        ),
    ]
