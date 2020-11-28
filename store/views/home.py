from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View 


class Index(View):
    def get(self,request):
        #First page reload korar somoy session cart object create
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.products_by_categoryid(categoryId)
        else:
            products = Product.get_all_products()

        context ={
            'products':products,
            'categories':categories
        }
        print('Your are: ',request.session.get('email'))
        return render(request, 'index.html', context)

    def post(self,request):
        #session add to cart 
        productId = request.POST.get('productId')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(productId)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(productId)
                    else:
                        cart[productId] = quantity-1
                else:
                    cart[productId] = quantity+1
            else:
                cart[productId] = 1
        else:
            cart = {}
            cart[productId] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('products-index')