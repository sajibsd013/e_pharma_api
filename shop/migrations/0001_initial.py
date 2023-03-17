# Generated by Django 3.2.15 on 2023-03-04 17:02

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('quantity', models.CharField(max_length=120, null=True)),
                ('offer', models.CharField(max_length=120, null=True)),
                ('price', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to=shop.models.upload_to_product)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Product',
                'db_table': 'product',
            },
        ),
    ]
