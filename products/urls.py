from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import ProductList,ProductDetail,CategoryList,BrandDetail,BrandList,add_review
from .api import ProductListApi,ProductDetailApi,BrandListApi,BrandDetailApi,CategoryListApi,CategoryDetailApi,ProductViewSets
# from .api import product_list_api ,product_detail_api


router = DefaultRouter()
router.register('v_set',ProductViewSets)


app_name = 'products'

urlpatterns =[
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('<int:pk>/add_review', add_review, name='add_review'),
    path('ctg/', CategoryList.as_view(), name='ctg_list'),
    path('brand/', BrandList.as_view(), name='brand_list'),
    path('brand/<slug:slug>', BrandDetail.as_view(), name='brand_detail'),


    #___API___
    # path('api', product_list_api),
    # path('api/<int:pk>', product_detail_api),

    path('api', ProductListApi.as_view()),
    path('api/<int:pk>', ProductDetailApi.as_view()),
    
    path('api/ctg', CategoryListApi.as_view()),
    path('api/ctg/<int:pk>', CategoryDetailApi.as_view()),

    path('api/brand', BrandListApi.as_view()),
    path('api/brand/<int:pk>', BrandDetailApi.as_view()),

    path('myapi/', include(router.urls)),

]