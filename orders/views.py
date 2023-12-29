from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Order ,OrderDetail,Cart,CartDetail,Coupon
from products.models import Products
from settings.models import DeleveryFee

from django.conf import settings


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

def remove_from_cart(request,id):
    cart= CartDetail.objects.get(id=id)
    cart.delete()
    return redirect('/products/')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user,status='in_progress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delvery_fee = DeleveryFee.objects.last().fee
    pub_key = settings.STRIPE_API_PUBLISHABLE_KEY

    if request.method == 'POST':
        coupon = get_object_or_404(Coupon,code=request.POST['coupon_code'])

        if coupon and coupon.quantity > 0:
            today_date = datetime.today().date()

            start_date = coupon.start_date.date()
            end_date = coupon.end_date.date()

            if today_date >= start_date and today_date <= end_date:
                total_value = cart.get_total()  
                discount =  total_value * coupon.discount / 100            
                total_after_discount =  total_value - discount

                coupon.quantity -= 1
                coupon.save()

                cart.coupon = coupon
                cart.total_after_coupon = total_after_discount
                cart.save()

                total = total_after_discount + delvery_fee

                cart = Cart.objects.get(user=request.user,status='in_progress')

                html = render_to_string('includes/coupon_table.html',{
                    'cart_detail':cart_detail,
                    'sub_total':total_after_discount,
                    'delvery_fee':delvery_fee,
                    'discount':discount ,
                    'total':total,
                    'pub_key':pub_key,
                })
                return JsonResponse({'html':html})

                # return render(request, 'orders/checkout.html', {
                #     'cart_detail':cart_detail,
                #     'sub_total':total_after_discount,
                #     'delvery_fee':delvery_fee,
                #     'discount':discount ,
                #     'total':total,
                # })
            
    else:
        total_value = cart.get_total()
        total = total_value + delvery_fee  
        discount = 0

    return render(request, 'orders/checkout.html',{
                'cart_detail':cart_detail,
                'sub_total':total_value,
                'delvery_fee':delvery_fee,
                'discount':discount ,
                'total':total,
                'pub_key':pub_key,    
            })


def payment_process(request):
    pass




