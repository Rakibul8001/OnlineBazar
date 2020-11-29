from django.db import models
from store.models.product import Product
from store.models.customer import Customer
from django.utils import timezone

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=50, default='', blank=True, null=True)
    address = models.CharField(max_length=50 ,default='', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    #Order save
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')