from django.shortcuts import render ,redirect
from django.urls import reverse 
from django.views import generic
from django.db.models.aggregates import Count
from .models import Products,Brand,Category,ProductReviews,ProductImage
from .forms import ReviewForm




class ProductList(generic.ListView):
    model = Products
    paginate_by = 20


    

class ProductDetail(generic.DetailView):
    model = Products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = ProductReviews.objects.all()
        return context


def add_review(request,id):
    product = Products.objects.get(id=id)
    if request.method == 'post':
        pod = ReviewForm(request.post)
        if pod.is_valid():
            form = pod.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect(reverse('products:product_detail', kwargs={'id':id}))
    

class CategoryList(generic.ListView):
    model = Category
    paginate_by = 20

    def get_queryset(self):
        queryset = super(CategoryList, self).get_queryset()
        queryset = Category.objects.all().annotate(product_num=Count('Category'))
        return queryset    


class BrandList(generic.ListView):
    model = Brand
    paginate_by = 20

    def get_queryset(self):
        queryset = super(BrandList, self).get_queryset()
        queryset = Brand.objects.all().annotate(product_num=Count('product_Brand'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ctgs"] = Category.objects.all()
        return context


    

class BrandDetail(generic.DetailView):
    model = Brand 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products.objects.all()
        return context