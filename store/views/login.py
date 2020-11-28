from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        #jodi customer thake
        if customer:
            #password check
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer_id']= customer.id
                # request.session['email'] = customer.email
                #jodi password match hoy
                return redirect('products-index')
            else:
                error_message = "Invalid email or password ..!"
        else:
            error_message = 'Invalid email or password!!'

        return render(request, 'login.html',{'error':error_message})

#Logout session
def logout(request):
    request.session.clear()
    return redirect('login')