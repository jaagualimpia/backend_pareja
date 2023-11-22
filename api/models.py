from django.db import models

# Create your models here.

class Order(models.Model):
    owner = models.CharField(max_length=50, default="Anonymous client")
    date = models.DateTimeField()
    total = models.FloatField()
    status = models.CharField(max_length=50)
    address = models.CharField(max_length=75)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=50)

class OrderToProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)