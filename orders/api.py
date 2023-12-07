from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Cart ,CartDetail,Order,OrderDetail,Coupon
from .serializer import CartSerializer,OrderDetailSerializer,OrderListSerializer,ProductOrderSerializer
from products.models import Products


#______Cart API__________
class CartListDetailAPI(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart,created = Cart.objects.get_or_create(user=user,status='in_progress')
        info =CartSerializer(cart).data
        return Response({'cart':info})


    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        quantity = int(request.POST['quantity'])
        product = Products.objects.get(id=request.data['product_id'])

        cart = Cart.objects.get(user=user,status='in_progress')
        cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)

        cart_detail.quantity = quantity
        cart_detail.total = round(quantity * product.price ,2)
        cart_detail.save()

        cart = Cart.objects.get(user=user,status='in_progress')
        info = CartSerializer(cart).data
        return Response({
            'messege':'user deleted sucessfully',
            'cart':info,
        })


    def delete(self,request,*args, **kwargs): 
        cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
        cart_detail.delete()

        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,status='in_progress')
        info = CartSerializer(cart).data
        return Response({
            'messege':'user deleted sucessfully',
            'cart':info,
        })




#________Order API ____________

class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    def list(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        info = OrderListSerializer(queryset,many=True).data
        return Response(info)
    
    # def get_queryset(self):
    #     queryset = super(OrderListAPI, self).get_queryset()
    #     user = User.objects.get(username=self.kwargs['username'])
    #     queryset = queryset.filter(user=user)
    #     return queryset


class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

class CreateOrderAPI(generics.GenericAPIView):
    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user)
        cart_detail = CartDetail.objects.filter(cart=cart)

        #  cart --> order
        new_order = Order.objects.create(
                user = user,
                coupon = cart.coupon,
                total_after_coupon = cart.total_after_coupon,
        )

        #  cart_detail --> order_detail 
        for item in cart_detail:
            OrderDetail.objects.create(
                order = new_order,
                product = item.product,
                price = item.product.price,
                quantity = item.quantity,
                total = round(int(item.quantity) * item.product.price ,2),
            )
        
        cart.status = 'completed'
        cart.save()
        return Response({'Messege':'Order Created Successfully'})
class ApplyCouponAPI(generics.GenericAPIView):
    pass
        
 