# Generated by Django 3.2.15 on 2022-09-27 08:49

import Specialist_Doctors.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialistDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('qualifications', models.TextField(null=True)),
                ('expericence', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('time', models.TextField(null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=Specialist_Doctors.models.upload_to_doctors)),
                ('speciality', models.CharField(max_length=100, null=True)),
                ('fee', models.CharField(max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Specialist Doctors List',
                'db_table': 'SpecialistDoctor',
            },
        ),
        migrations.CreateModel(
            name='SpecialistDoctorsAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120)),
                ('patient_age', models.CharField(max_length=120)),
                ('patient_phone', models.CharField(max_length=120)),
                ('details', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Specialist_Doctors.specialistdoctor', verbose_name='Doctor ID')),
            ],
            options={
                'verbose_name_plural': 'Specialist Doctors Appointment',
                'db_table': 'SpecialistDoctorsAppointment',
            },
        ),
    ]