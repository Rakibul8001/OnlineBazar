from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
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
        #customer object
        customer = Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
        #calling validateCustomer method
        error_message = self.validateCustomer(customer)
        #saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("products-index")
        else:
            context={
                'error':error_message,
                'values':value
            }
            return render(request, 'signup.html',context)
    
    def validateCustomer(self,customer):
        error_message = None
        if not customer.first_name:
            error_message = 'First name must be filled'
        elif len(customer.first_name)<4:
            error_message='First name should be more than 4 char'
        elif not customer.last_name:
            error_message = 'Last name required'
        elif len(customer.last_name)<4:
            error_message='Last name should be at least 4 char'
        elif not customer.phone:
            error_message = 'Phone number required'
        elif len(customer.phone)<4:
            error_message='Phone number should be at least 11 char'
        elif not customer.email:
            error_message = 'Email is required'
        elif not customer.password:
            error_message="Password is required"
        elif len(customer.password)<6:
            error_message = "Password mush be at least 6 char"
        elif customer.isExists():
            error_message='Email address has already exists..!'

        return error_message
