# Generated by Django 4.2.7 on 2024-03-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedapp', '0007_passwordreset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bed_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_id',
            field=models.CharField(max_length=10),
        ),
    ]
