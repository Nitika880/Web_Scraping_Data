# Generated by Django 3.2.5 on 2023-02-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_scrap_links_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap_links',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]