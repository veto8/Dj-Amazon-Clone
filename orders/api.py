from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Cart ,CartDetail
from .serializer import CartSerializer
from products.models import Products

class CartListDetailAPI(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart,created = Cart.objects.get_or_create(user=user,status='in_progress')
        info = CartSerializer(cart).data
        return Response({'cart':info})


    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Products.objects.get(id=request.data['product_id'])
        quantity = int(request.POST['quantity'])
        cart = Cart.objects.get(user=user,status='in_progress')
        cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)

        product.quantity = quantity
        product.total = round(quantity * product.price)
        product.save()

        cart = Cart.objects.get(user=user,status='in_progress')
        info = CartSerializer(cart).data
        return Response({
            'messege':'you deleted this product sucessfully',
            'cart':cart,
        })



    def delete(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
        cart_detail.delete()

        cart = Cart.objects.get(user=user,status='in_prgress')
        info = CartSerializer(info).data
        return Response({
            'messege':'you deleted this product sucessfully',
            'cart':cart,
        })


