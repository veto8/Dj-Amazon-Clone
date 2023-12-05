from rest_framework import serializers
from .models import Cart,CartDetail
from products.serializers import ProductSerializer


class CartDetailSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    product = serializers.StringRelatedField()
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'


