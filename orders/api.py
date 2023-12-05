from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Cart ,CartDetail
from .serializer import CartSerializer

class CartListDetailAPI(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart,created = Cart.objects.get_or_create(user=user,status='in_progress')
        info = CartSerializer(cart).data
        return Response({'cart':info})


    def post(self,request,*args, **kwargs):
        pass

    def delete(self,request,*args, **kwargs):
        pass


