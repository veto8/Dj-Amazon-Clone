from django_filters import rest_framework as filters
import django_filters
from .models import Products


class ProductFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Products
        fields = {

            'price': ['range', 'gte', 'lte']
        }

