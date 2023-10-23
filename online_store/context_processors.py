from product.models import Product

def get_all_products(request):
    return {'products': Product.objects.all()}
