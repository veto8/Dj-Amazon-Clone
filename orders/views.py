from django.views import generic

from django.shortcuts import render
from .models import Order ,OrderDetail,Cart,CartDetail


class OrderList(generic.ListView):
    model = Order
    paginate_by = 4

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
