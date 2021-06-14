from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
