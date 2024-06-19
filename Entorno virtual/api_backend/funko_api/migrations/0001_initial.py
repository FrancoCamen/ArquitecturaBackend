# Generated by Django 5.0.3 on 2024-05-13 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('number', models.IntegerField()),
                ('collection', models.CharField(max_length=50)),
                ('is_backlight', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('funkos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funko_api.funko')),
            ],
        ),
    ]
