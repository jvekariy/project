"""
URL configuration for shopproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopapp import views

urlpatterns = [

    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('cart_add/<int:id>', views.cart_add, name='cart_add'),
    path('cart_delete/<int:id>', views.cart_delete, name='cart_delete'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('men', views.men, name='men'),
    path('order_complete', views.order_complete, name='order_complete'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('women', views.women, name='women'),
    path('login', views.login, name='login'),
    path('register_from', views.register_from, name='register_from'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('search', views.search, name='search'),
    path('review', views.review, name='review'),
    path('add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
    path('rating', views.rating, name='rating'),
    path('cart_plus/<int:id>', views.cart_plus, name='cart_plus'),
    path('cart_minus/<int:id>', views.cart_minus, name='cart_minus'),
    path('category_page', views.category_page, name='category_page'),
    path('forgate_password', views.forgate_password, name='forgate_password'),
    path('confirm_password', views.confirm_password, name='confirm_password'),

    path('wishlist_delete/<int:id>', views.wishlist_delete, name='wishlist_delete'),


]
