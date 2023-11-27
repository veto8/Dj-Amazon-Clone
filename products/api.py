from rest_framework import generics

from .serializers import ProductSerializer, CategorySerializer, BrandSerializer,CategoryDetailSerializer,BrandDetailSerializer
from .models import Products , Brand, Category 



class ProductListApi(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer



class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailApi(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer



class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer



# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def product_list_api(request):
#     prod = Products.objects.all()
#     data = ProductSerializer(prod, many=True).data
#     return Response({
#         'success':True,
#         'product_list':data,
#     })
# @api_view(['GET'])
# def product_detail_api(request,id):
#     prod = Products.objects.get(id=id)
#     data = ProductSerializer(prod).data
#     return Response({
#         'success': True,
#         'product_detail':data,
#     })