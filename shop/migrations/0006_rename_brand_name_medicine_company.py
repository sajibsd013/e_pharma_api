# Generated by Django 3.2.15 on 2023-04-29 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_medicine_medicine_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='brand_name',
            new_name='company',
        ),
    ]