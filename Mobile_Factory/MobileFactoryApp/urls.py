from django.contrib import admin
from django.urls import path, include
from .views import create_order

urlpatterns = [
    path("orders", create_order,name ='create_order'),
]