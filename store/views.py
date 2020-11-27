from django.shortcuts import render,redirect
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

        #values
        value = {
            'first_name': first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }

        #validation
        error_message = None
        customer = Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
        if not first_name:
            error_message = 'First name must be filled'
        elif len(first_name)<4:
            error_message='First name should be more than 4 char'
        elif not last_name:
            error_message = 'Last name required'
        elif len(last_name)<4:
            error_message='Last name should be at least 4 char'
        elif not phone:
            error_message = 'Phone number required'
        elif len(phone)<4:
            error_message='Phone number should be at least 11 char'
        elif not email:
            error_message = 'Email is required'
        elif not password:
            error_message="Password is required"
        elif len(password)<6:
            error_message = "Password mush be at least 6 char"
        elif customer.isExists():
            error_message='Email address has already exists..!'

        #saving
        if not error_message:
            customer.register()
            return redirect("products-index")
        else:
            context={
                'error':error_message,
                'values':value
            }
            return render(request, 'signup.html',context)