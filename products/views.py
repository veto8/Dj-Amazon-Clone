from django.shortcuts import render
from django.views import generic
from django.db.models.aggregates import Count
from .models import Products,Brand,Category,ProductReviews,ProductImage




class ProductList(generic.ListView):
    model = Products
    paginate_by = 20

class ProductDetail(generic.DetailView):
    model = Products



class CategoryList(generic.ListView):
    model = Category
    paginate_by = 10
    


class BrandList(generic.ListView):
    model = Brand
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ctgs"] = Category.objects.all()
        context['brand_list'] = Brand.objects.all().annotate(product_num=Count('product_Brand'))
        return context
    

class BrandDetail(generic.DetailView):
    model = Brand