from django.urls import path
from .views import ProductList,ProductDetail,CategoryList,BrandDetail,BrandList
from .api import ProductListApi,ProductDetailApi,BrandListApi,BrandDetailApi,CategoryListApi
# from .api import product_list_api ,product_detail_api
app_name = 'products'

urlpatterns =[
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('ctg', CategoryList.as_view(), name='ctg_list'),
    path('brand', BrandList.as_view(), name='brand_list'),
    path('brand/<int:pk>', BrandDetail.as_view(), name='brand_detail'),

    #___API___
    # path('api', product_list_api),
    # path('api/<int:pk>', product_detail_api),

    path('api', ProductListApi.as_view()),
    path('api/<int:pk>', ProductDetailApi.as_view()),
    path('api/ctg', CategoryListApi.as_view()),
    path('api/brand', BrandListApi.as_view()),
    path('api/brand/<int:pk>', BrandDetailApi.as_view()),



]