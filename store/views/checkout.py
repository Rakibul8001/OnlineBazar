from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from store.models.orders import Order

class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        # print(address, phone, customer,cart,products)

        for product in products:
            #create order object
            order = Order(
                customer = Customer(id=customer),
                product = product,
                price = product.price,
                phone = phone,
                address = address,
                quantity = cart.get(str(product.id))
            )
            #order save
            order.placeOrder()
        #cart clear
        request.session['cart'] ={}
        return redirect('cart')