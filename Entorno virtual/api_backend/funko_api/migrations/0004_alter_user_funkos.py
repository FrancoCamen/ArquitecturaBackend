# Generated by Django 5.0.3 on 2024-06-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0003_remove_user_funkos_user_funkos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='funkos',
            field=models.ManyToManyField(blank=True, to='funko_api.funko'),
        ),
    ]
