# Generated by Django 3.2.15 on 2022-11-07 06:28

from django.db import migrations, models
import partners.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0017_auto_20221106_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dmf_doctor',
            old_name='fee_video_call',
            new_name='fee',
        ),
        migrations.RenameField(
            model_name='dmf_doctor',
            old_name='whatsapp_number',
            new_name='working_days',
        ),
        migrations.RenameField(
            model_name='dmf_doctor',
            old_name='working_days_home_call',
            new_name='working_times',
        ),
        migrations.RemoveField(
            model_name='dmf_doctor',
            name='working_days_video_call',
        ),
        migrations.RemoveField(
            model_name='dmf_doctor',
            name='working_times_chamber',
        ),
        migrations.RemoveField(
            model_name='dmf_doctor',
            name='working_times_home_call',
        ),
        migrations.RemoveField(
            model_name='dmf_doctor',
            name='working_times_video_call',
        ),
        migrations.AddField(
            model_name='dmf_doctor',
            name='certificate',
            field=models.ImageField(null=True, upload_to=partners.models.upload_to_certificate),
        ),
    ]