# Generated by Django 3.2.5 on 2023-02-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20230201_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon_data',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
