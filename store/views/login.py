from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
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
                #eta use korci middleware er por order page theke login page , tarpor login korar por abr direct order page e jawar jonno(go middleware>auth)
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    # r jodi kono url na thake, direct index page e
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