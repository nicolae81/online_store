# Create your views here.
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from orders.models import OrderCart
from product.models import Product


class OrderCartListView(ListView):
    model = OrderCart
    template_name = 'orders/cart_list.html'
    context_object_name = 'cart_products'

    def get_queryset(self):
        result = (OrderCart.objects.filter(cart_item=1, user_id=self.request.user.id))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for product in OrderCart.objects.filter(user_id=self.request.user.id):
            total += product.amount
        context['total'] = total



        return context


@login_required()
def add_to_cart(request, pk):


    # verificam daca produsul este in cosul de cumparaturi
    if OrderCart.objects.filter(user_id=request.user.id,
                                product_id=pk).exists():
        current = OrderCart.objects.get(product_id=pk, user_id=request.user.id)
        quantity = current.quantity + 1

        amount = current.product.price * quantity
        OrderCart.objects.filter(user_id=request.user.id,
                                 product_id=pk).update(quantity=quantity, amount=amount)
    else:
        # adauga produsul in cosul de cumparaturi
        quantity = 1
        current = Product.objects.get(id=pk)

        amount = current.price * 1
        OrderCart.objects.create(
            user_id=request.user.id,
            product_id=pk,
            cart_item=True,
            quantity=quantity,
            amount= amount,
            created_at=datetime.now()
        )

    return redirect('products-by-category', pk)


class CartListView(ListView):
    template_name = 'orders/cart_list.html'
    model = OrderCart
    context_object_name = 'cart_products'

    def get_queryset(self):
        return OrderCart.objects.filter(cart_item=1)
