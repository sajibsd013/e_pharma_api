# Generated by Django 3.2.15 on 2023-01-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('depertment', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('salary', models.CharField(max_length=120)),
                ('last_date', models.DateTimeField(blank=True, null=True)),
                ('working_schedule', models.CharField(max_length=120)),
                ('job_nature', models.CharField(max_length=120)),
                ('requirements', models.TextField()),
                ('responsibilities', models.TextField()),
                ('benefits', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Job',
                'db_table': 'Job',
            },
        ),
    ]
