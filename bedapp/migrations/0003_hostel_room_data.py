# Generated by Django 4.2.7 on 2024-03-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedapp', '0002_remove_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='room_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
