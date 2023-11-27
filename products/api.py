from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from .models import Products , Brand, Category 

@api_view(['GET'])
def product_list_api(request):
    prod = Products.objects.all()
    data = ProductSerializer(prod, many=True).data
    return Response({
        'success':True,
        'product_list':data,
    })
@api_view(['GET'])
def product_detail_api(request,id):
    prod = Products.objects.get(id=id)
    data = ProductSerializer(prod).data
    return Response({
        'success': True,
        'product_detail':data,
    })



class ProductListApi(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CategoryListApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandListApi(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer