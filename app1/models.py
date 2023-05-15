from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Amazon_Data(models.Model):
    title = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    details = models.TextField()
    image = models.URLField(null=True, blank=True)


class Flipkart_Data(models.Model):
    title = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    price = models.IntegerField()
    details = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    image = models.URLField(null=True, blank=True)


class Scrap_links(models.Model):
    link = models.URLField(max_length=1000)
    product_type = models.CharField(max_length=255)
    website = models.CharField(max_length=255, null=True, blank=True)

