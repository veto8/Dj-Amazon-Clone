from django_filters import rest_framework as filters
from .models import Products


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Products
        fields = {
            'name': ['icontains'],
            'price': ['range', 'gte', 'lte']
        }

