from rest_framework import generics, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer, CategorySerializer, BrandSerializer,CategoryDetailSerializer,BrandDetailSerializer
from .models import Products , Brand, Category 
from .myfilter import ProductFilter
from .mypagination import MyPagination



class ProductListApi(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['name', 'category']
    search_fields = ['name', 'price']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    
    
class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]



class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['name', ]
    search_fields = ['name', ]
    ordering_fields = ['name', ]
    permission_classes = [IsAuthenticated]

class CategoryDetailApi(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]



class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['name', 'category']
    search_fields = ['name', ]
    ordering_fields = ['category', ]
    permission_classes = [IsAuthenticated]

class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    permission_classes = [IsAuthenticated]


#____sets viwe _____

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer





#_____function view______

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