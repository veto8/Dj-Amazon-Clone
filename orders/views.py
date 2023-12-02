from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Order ,OrderDetail,Cart,CartDetail


class OrderList(generic.ListView,LoginRequiredMixin):
    model = Order
    paginate_by = 4

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user,status='in_progress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    return render(request, 'orders/checkout.html',{
        'cart_detail':cart_detail,
    })
