# Generated by Django 4.2.7 on 2024-03-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedapp', '0008_alter_booking_bed_id_alter_booking_room_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel',
            name='norooms',
        ),
        migrations.AlterField(
            model_name='hostel',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
