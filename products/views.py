from django.shortcuts import render ,redirect
from django.urls import reverse 
from django.views import generic
from django.db.models.aggregates import Count
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Products,Brand,Category,ProductReviews
from .tasks import test_celery
from .myfilter import ProductFilter




def test(request):
    data = Products.objects.all()[:5]

    test_celery.delay()
    return render ( request,'products/test.html',{'data':data})

class ProductList(generic.ListView):
    model = Products
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        myfilter = ProductFilter(self.request.GET, queryset=queryset)
        return myfilter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myfilter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

   

class ProductDetail(generic.DetailView):
    model = Products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = ProductReviews.objects.filter(product=self.get_object())
        context['related_products'] = Products.objects.filter(brand=self.get_object().brand)[0:10]
        return context

    

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


    

class BrandDetail(generic.ListView):
    model = Products
    paginate_by = 15 
    template_name = 'products/brand_detail.html'
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] =Brand.objects.get(slug=self.kwargs['slug'])
        return context
    

def add_review(request,slug):
    product = Products.objects.get(slug=slug)

    rate = request.POST['rate']         #  rate = request.POST.get('rate') ,  rate = request.GET.get('rate') 
    review = request.POST['review']

        # Check if the user is authenticated
    if request.user.is_authenticated:
        user = request.user
    else:
        # Handle the case of an anonymous user, you can set user to None or any default value
        user = None

    ProductReviews.objects.create(
        product = product,
        rate = rate,
        feedback = review,
        user = user, 
    )

    reviews = ProductReviews.objects.filter(product=product)
    html = render_to_string('includes/review.html',{'reviews':reviews})
    return JsonResponse({'html':html})

