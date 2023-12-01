from .models import Cart ,CartDetail 

def cart_info(request):
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user,status='in_progress')
        if not created:
            cart_detail = CartDetail.objects.filter(cart=cart)
            return {'cart_data':cart,'cart_detail_data':cart_detail}
        else:
            return {'cart_data':cart}
    else:    
        return {}