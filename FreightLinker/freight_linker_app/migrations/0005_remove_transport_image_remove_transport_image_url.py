# Generated by Django 4.0 on 2024-02-20 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freight_linker_app', '0004_users_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='image',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='image_url',
        ),
    ]
