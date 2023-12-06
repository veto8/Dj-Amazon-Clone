from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Cart ,CartDetail,Order,OrderDetail,Coupon
from .serializer import CartSerializer,OrderDetailSerializer,OrderListSerializer,ProductOrderSerializer
from products.models import Products

class CartListDetailAPI(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart,created = Cart.objects.get_or_create(user=user,status='in_progress')
        info =CartSerializer(cart).data
        return Response({'cart':info})


    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        quantity = request.POST['quantity']
        product = Products.objects.get(id=request.data['product_id'])

        cart = Cart.objects.get(user=user,status='in_progress')
        cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)

        cart_detail.quantity = int(quantity)
        cart_detail.total = round(int(quantity) * product.price ,2)
        cart_detail.save()

        cart = Cart.objects.get(user=user,status='in_progress')
        info = CartSerializer(cart).data
        return Response({
            'messege':'user deleted sucessfully',
            'cart':info,
        })


    def delete(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
        cart_detail.delete()

        cart = Cart.objects.get(user=user,status='in_progress')
        info = CartSerializer(cart).data
        return Response({
            'messege':'user deleted sucessfully',
            'cart':info,
        })


class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    def list(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        info = OrderListSerializer(queryset,many=True).data
        return Response(info)

