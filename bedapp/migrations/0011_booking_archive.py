# Generated by Django 4.2.7 on 2024-03-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedapp', '0010_user_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phone', models.IntegerField()),
                ('hostel_name', models.CharField(max_length=255)),
                ('room_id', models.CharField(max_length=10)),
                ('bed_id', models.CharField(max_length=10)),
                ('bed_price_per_day', models.CharField(max_length=50)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
            ],
        ),
    ]
