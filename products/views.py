from django.shortcuts import render
from django.views import generic
from .models import Products,Brand,Category,ProductReviews,ProductImage



class ProductList(generic.ListView):
    model = Products

class ProductDetail(generic.DetailView):
    model = Products



class CategoryList(generic.ListView):
    model = Category



class BrandList(generic.ListView):
    model = Brand

class BrandDetail(generic.DetailView):
    model = Brand