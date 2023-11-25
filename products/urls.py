from django.urls import path
from .views import ProductList,ProductDetail,CategoryList,BrandDetail,BrandList

app_name = 'products'

urlpatterns =[
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('ctg', CategoryList.as_view(), name='ctg_list'),
    path('brand', BrandList.as_view()),
    path('brand/<int:pk>', BrandDetail.as_view()),
]