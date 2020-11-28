from django.urls import path
from .views import home,login,signup,cart

urlpatterns = [
    path('',home.Index.as_view(), name='products-index'),
    path('signup',signup.Signup.as_view(), name='signup'),
    path('login',login.Login.as_view(), name='login'),
    path('logout',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(), name='cart'),
]
