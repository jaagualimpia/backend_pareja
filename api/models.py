from django.db import models

# Create your models here.

class Order(models.Model):
    date = models.DateTimeField()
    total = models.FloatField()
    status = models.CharField(50)
    address = models.CharField(75)

class Product(models.Model):
    name = models.CharField(50)
    price = models.FloatField()
    description = models.CharField(50)

class OrderToProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)