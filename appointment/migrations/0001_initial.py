# Generated by Django 3.2.15 on 2022-11-19 07:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0021_alter_dmf_doctor_type'),
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
                ('details', models.TextField()),
                ('date', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.doctor', verbose_name='Doctor')),
            ],
            options={
                'verbose_name_plural': 'Doctors Appointment',
            },
        ),
    ]
