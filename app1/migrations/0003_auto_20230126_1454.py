# Generated by Django 3.2.5 on 2023-01-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230126_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazon_data',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flipkart_data',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]