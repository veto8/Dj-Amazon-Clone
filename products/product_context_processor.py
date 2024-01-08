from .models import Products,Category

def product_info(request):
    product = Products.objects.all()
    categories= Category.objects.all().order_by('name')
    return {
        'product':product,
        'ctgs':categories,
    }