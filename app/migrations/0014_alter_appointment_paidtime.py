# Generated by Django 3.2.5 on 2023-05-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_appointment_paidtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='paidTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
