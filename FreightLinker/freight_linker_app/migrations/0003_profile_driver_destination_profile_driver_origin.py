# Generated by Django 4.0 on 2024-02-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freight_linker_app', '0002_profile_driver_user_id_user_profile_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_driver',
            name='destination',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile_driver',
            name='origin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
