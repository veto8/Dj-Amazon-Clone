from rest_framework import serializers
from .models import Cart,CartDetail,Order,OrderDetail
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


#_____order serializer _________

class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'

class ProductOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    product = ProductOrderSerializer()
    class Meta:
        model = Order
        fields = '__all__'