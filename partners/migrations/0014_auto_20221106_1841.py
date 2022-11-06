# Generated by Django 3.2.15 on 2022-11-06 12:41

from django.db import migrations, models
import partners.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0013_auto_20221106_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregiver',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='payment_method',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='caregiver',
            name='payment_number',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='physiotherapist',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='physiotherapist',
            name='payment_method',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='physiotherapist',
            name='payment_number',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='dmf_doctor',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=partners.models.upload_to_doctor),
        ),
    ]
