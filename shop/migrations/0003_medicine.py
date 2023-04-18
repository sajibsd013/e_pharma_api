# Generated by Django 3.2.15 on 2023-04-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=120)),
                ('weight', models.CharField(max_length=120)),
                ('medicine_type', models.CharField(choices=[('Tablet', 'Tablet'), ('Capsule', 'Capsule'), ('Injection', 'Injection'), ('Pediatric Drop', 'Pediatric Drop'), ('Suspension', 'Suspension'), ('Powder for Suspension', 'Powder for Suspension'), ('IV Injection', 'IV Injection'), ('Cream', 'Cream'), ('Gel', 'Gel'), ('Infusion', 'Infusion'), ('Nebulizer  Solution', 'Nebulizer  Solution'), ('Syrup', 'Syrup'), ('Sachet', 'Sachet'), ('Eye Drop', 'Eye Drop'), ('Eye Oinment', 'Eye Oinment')], max_length=120)),
                ('brand_name', models.CharField(max_length=120)),
                ('unit_price', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'medicine',
                'db_table': 'medicine',
            },
        ),
    ]
