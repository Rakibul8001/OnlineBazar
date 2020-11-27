from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View 


class Index(View):
    def get(self,request):
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
        # print('Your are: ',request.session.get('email'))
        return render(request, 'index.html', context)

    def post(self,request):
        productId = request.POST.get('productId')
        print(productId)
        return redirect('products-index')