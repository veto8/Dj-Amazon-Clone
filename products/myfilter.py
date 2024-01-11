from django_filters import rest_framework as filters
import django_filters
from django import forms
from django.db import models
from .models import Products

 
class ProductFilter(filters.FilterSet):
    name = django_filters.CharFilter(
        label='Product Name',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder':'search here'})
    )
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Products
        fields = ['name','brand','category','flag']


