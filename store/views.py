from django.shortcuts import render
from .models.product import Product
from .models.category import Category

# Create your views here.
def index(request):
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
    return render(request, 'index.html', context)