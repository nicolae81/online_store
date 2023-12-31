# Create your views here.
from datetime import datetime
from pprint import pprint
from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from orders.forms import PlaceOrderForm
from orders.models import OrderCart, PlaceOrder
from product.models import Product


class CartListView(ListView):
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
            amount=amount,
            created_at=datetime.now()
        )

    return redirect('products-by-category', pk)


class WishListView(ListView):
    model = OrderCart
    template_name = 'orders/wish_list.html'
    context_object_name = 'wish_products'

    def get_queryset(self):
        result = (OrderCart.objects.filter(wishlist_item=1, user_id=self.request.user.id))
        return result


@login_required()
def add_to_wishlist(request, pk):
    if OrderCart.objects.filter(user_id=request.user.id,
                                product_id=pk,
                                wishlist_item=True).exists():

        return redirect('wish-list')
    else:
        OrderCart.objects.create(
            user_id=request.user.id,
            product_id=pk,
            cart_item=False,
            wishlist_item=True,
            quantity=1,
            amount=Product.objects.get(id=pk).price,
            created_at=datetime.now()
        )
        return redirect('wish-list')


@login_required()
def increase_quantity(request, pk):
    cart_product = get_object_or_404(OrderCart, product_id=pk, user_id=request.user.id)
    cart_product.quantity += 1
    cart_product.amount = cart_product.product.price * cart_product.quantity
    cart_product.save()
    return redirect('cart-list')


@login_required()
def decrease_quantity(request, pk):
    cart_product = get_object_or_404(OrderCart, product_id=pk, user_id=request.user.id)
    if cart_product.quantity > 1:
        cart_product.quantity -= 1
        cart_product.amount = cart_product.product.price * cart_product.quantity
        cart_product.save()
    else:
        cart_product.delete()
    return redirect('cart-list')


@login_required()
def move_favorites_to_cart(request, pk):

    current_order = OrderCart.objects.get(user_id=request.user.id, id=pk)
    amount = current_order.quantity * current_order.product.price
    OrderCart.objects.filter(user_id=request.user.id, id=pk).update(cart_item=1, wishlist_item=1, amount=amount)

    return redirect('cart-list')


@login_required()
def delete_from_cart(request, pk):
    if OrderCart.objects.filter(user_id=request.user.id, id=pk, wishlist_item=1).exists():
        OrderCart.objects.filter(user_id=request.user.id, id=pk).update(cart_item=0)
        return redirect('cart-list')
    else:
        OrderCart.objects.filter(user_id=request.user.id, id=pk).delete()

    return redirect('cart-list')


@login_required()
def delete_from_wishlist(request, pk):
    if OrderCart.objects.filter(user_id=request.user.id, id=pk, cart_item=1).exists():
        OrderCart.objects.filter(user_id=request.user.id, id=pk).update(wishlist_item=0)
        return redirect('wish-list')
    else:
        OrderCart.objects.filter(user_id=request.user.id, id=pk).delete()

    return redirect('wish-list')


# create json
class PlaceOrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'orders/place_order.html'
    model = PlaceOrder
    form_class = PlaceOrderForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            new_order = form.save(commit=False)

            # user_id
            new_order.user_id = self.request.user.id

            # order number
            generic_order = randint(1, 100)
            new_order.order_number = f'ESHOP_{generic_order}'

            # product list
            products = {'data': []}
            final_price = 0
            products_per_user = OrderCart.objects.filter(user_id=self.request.user.id, cart_item=1)

            for item in products_per_user:
                products['data'].append({'title': item.product.title,
                                         'quantity': item.quantity,
                                         'price': f'{item.product.price * item.quantity}'
                                         })

            final_price += item.product.price * item.quantity
            new_order.product_list = products
            pprint(products)

            # price
            new_order.price = final_price

            # invoice_address

            new_order.invoice_address = new_order.delivery_address

            # created_at

            new_order.created_at = datetime.now()

            new_order.save()

            return redirect('home_page')
