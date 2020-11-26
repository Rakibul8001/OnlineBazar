from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

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

def signup(request):
    if request.method =='GET':
        return render(request, 'signup.html')
    else:
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
        customer.register()
        return HttpResponse("Your account has created successfully")