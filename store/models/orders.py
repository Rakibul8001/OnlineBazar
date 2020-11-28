from django.db import models
from store.models.product import Product
from store.models.customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=50, default='', blank=True, null=True)
    address = models.CharField(max_length=50 ,default='', blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)