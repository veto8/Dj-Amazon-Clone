from .models import Cart ,CartDetail 

def cart_info(request):
    cart_detail = CartDetail.objects.all()
    return {'cart_detail':cart_detail}
