# Generated by Django 4.1.5 on 2023-06-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmark_events', '0005_alter_landmarkevent_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmarkevent',
            name='end_date',
            field=models.DateTimeField(default='9999-12-30 59:59:59.314354+00:00'),
        ),
    ]
