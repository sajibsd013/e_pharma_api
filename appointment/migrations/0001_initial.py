# Generated by Django 3.2.15 on 2023-01-24 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120)),
                ('patient_age', models.CharField(max_length=120)),
                ('patient_phone', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('fee', models.CharField(max_length=120)),
                ('date', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('payment_method', models.CharField(choices=[('Bkash', 'Bkash'), ('Nogod', 'Nogod'), ('Rocket', 'Rocket'), ('Upay', 'Upay')], default='Bkash', max_length=120)),
                ('transaction_id', models.CharField(blank=True, max_length=120, null=True)),
                ('payment_status', models.CharField(choices=[('unpaid', 'unpaid'), ('pending', 'pending'), ('paid', 'paid')], default='unpaid', max_length=120)),
                ('service_status', models.CharField(choices=[('pending', 'pending'), ('cancelled', 'cancelled'), ('completed', 'completed'), ('approved', 'approved')], default='approved', max_length=120)),
                ('details', models.TextField()),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='partners.doctor', verbose_name='Doctor')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Doctors Appointment',
            },
        ),
    ]
