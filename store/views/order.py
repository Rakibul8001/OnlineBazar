from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from store.models.orders import Order

class OrderView(View):
    def get(self,request):
        customer = request.session.get('customer_id')
        orders = Order.get_order_by_customer(customer)
        print(orders)
        return render(request,'orders.html')
        