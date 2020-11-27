from django.urls import path
from .views import home,login,signup

urlpatterns = [
    path('',home.Index.as_view(), name='products-index'),
    path('signup',signup.Signup.as_view(), name='signup'),
    path('login',login.Login.as_view(), name='login'),
]
