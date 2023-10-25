
from category.models import Category
from product.models import Product


def get_all_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_all_product(request):
    products = Product.objects.all()
    return {'products': products}

