from rest_framework import serializers
from .models import Products,Brand,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    price_after_descount = serializers.SerializerMethodField(method_name='price_with_dis')
    # brand = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()
    def price_with_dis(self,product):
        return (product.price - product.price* 0.10)
    class Meta:
        model = Products
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source ='Category',many=True )
    class Meta:
        model = Category
        fields = '__all__'




