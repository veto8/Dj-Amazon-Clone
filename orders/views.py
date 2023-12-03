from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from .models import Order ,OrderDetail,Cart,CartDetail
from products.models import Products


class OrderList(LoginRequiredMixin,generic.ListView):
    model = Order
    paginate_by = 4

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    

def add_to_cart(request):
    quantity = request.POST['quantity']
    product = Products.objects.get(id=request.POST['product_id'])

    cart = Cart.objects.get(user=request.user,status='in_progress')
    cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)

    cart_detail.quantity = int(quantity)
    cart_detail.total = round(int(quantity) * product.price,2)
    cart_detail.save()

    return redirect(f'/products/{product.slug}')

def delete_product_cart(request):
    ''


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user,status='in_progress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    return render(request, 'orders/checkout.html',{
        'cart_detail':cart_detail,
    })
