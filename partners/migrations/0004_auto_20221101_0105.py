# Generated by Django 3.2.15 on 2022-10-31 19:05

from django.db import migrations, models
import partners.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_alter_dmf_doctor_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmf_doctor',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=partners.models.upload_to_doctor),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='city',
            field=models.CharField(blank=True, default='N/A', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='working_area',
            field=models.CharField(blank=True, default='N/A', max_length=500, null=True),
        ),
    ]