# Generated by Django 3.2.5 on 2023-05-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230518_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Bio',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='translatorr',
            name='Bio',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
