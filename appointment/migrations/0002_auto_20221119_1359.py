# Generated by Django 3.2.15 on 2022-11-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorsappointment',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'pending'), ('paid', 'paid')], default='pending', max_length=120),
        ),
        migrations.AddField(
            model_name='doctorsappointment',
            name='service_status',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved')], default='pending', max_length=120),
        ),
    ]
