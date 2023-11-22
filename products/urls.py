from django.urls import path
from .views import ProductList,ProductDetail,CategoryList,BrandDetail,BrandList

app_name = 'products'

urlpatterns =[
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('ctg/list', CategoryList.as_view(), name='ctg_list'),
    path('brand/list', BrandList.as_view()),
    path('brand/detail', BrandDetail.as_view()),
]