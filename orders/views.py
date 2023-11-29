from django.views import generic

from django.shortcuts import render
from .models import Order ,OrderDetail,Cart,CartDetail


class OrderList(generic.ListView):
    model = Order
