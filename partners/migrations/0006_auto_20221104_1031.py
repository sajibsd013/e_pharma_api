# Generated by Django 3.2.15 on 2022-11-04 04:31

from django.db import migrations, models
import partners.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0005_alter_dmf_doctor_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='dmf_doctor',
            name='payment_method',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='dmf_doctor',
            name='payment_number',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='dmf_doctor',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=partners.models.upload_to_doctor),
        ),
        migrations.AlterField(
            model_name='dmf_doctor',
            name='institution_or_chamber_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dmf_doctor',
            name='working_area',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
