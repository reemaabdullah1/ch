# Generated by Django 3.2.5 on 2023-05-23 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230523_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='translatorr',
            name='avatar',
        ),
    ]
