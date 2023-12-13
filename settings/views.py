from django.shortcuts import render
from .models import Company
from django.db.models import Count
from products.models import Products,Brand,Category,ProductReviews
from django.views.decorators.cache import cache_page


# @cache_page(60 * 1)
def home(request):
    sale_product = Products.objects.filter(flag='Sale')[:10]
    feature_product = Products.objects.filter(flag='Feature')[0:6]
    new_product = Products.objects.filter(flag='New')[0:10]
    product = Products.objects.filter(flag='New')[20:30]
    review = ProductReviews.objects.all()
    brand = Brand.objects.all()
    category = Category.objects.all().annotate(product_num=Count('Category'))

    return render(request,'settings/home.html',{
        'product':product,
        'product_sale':sale_product,
        'products_fea':feature_product,
        'product_new':new_product,
        'review':review,
        'ctgs':category,
        'brands':brand,
    } )
