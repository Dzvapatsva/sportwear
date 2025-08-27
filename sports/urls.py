from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('/shopping', views.shopping, name='shopping'),
    path('/cart', views.cart, name='cart'),
path('/contact', views.contact, name='contact')
]
