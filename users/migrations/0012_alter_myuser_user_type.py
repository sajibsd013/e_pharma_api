# Generated by Django 3.2.15 on 2022-12-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20221122_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('doctor', 'doctor'), ('nurse', 'nurse'), ('caregiver', 'caregiver'), ('physiotherapist', 'physiotherapist'), ('partner ', 'partner '), ('patient', 'patient')], default='patient', max_length=120),
        ),
    ]
