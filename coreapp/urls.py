
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index, name=""),
      path('products',views.products, name="products"),
]
