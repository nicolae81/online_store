from urllib import request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Product
from manage_users.models import History
from product.filters import ProductFilter
from django.shortcuts import render
from product.models import Product
from product.forms import ProductForm, ProductUpdateForm
from datetime import datetime


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list-products')
    success_message = 'Produsul {pname} a fost adaugat cu success.'
    permission_required = 'product.add_product'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(pname=self.object.title)

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            history_text = f'{new_product.title} was successfully created on {datetime.now()}'

            History.objects.create(text=history_text)
        return redirect('list-products')


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/list_products.html'
    model = Product
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_all_products = Product.objects.all()
        filters = ProductFilter(self.request.GET, queryset=get_all_products)
        context['all_products'] = filters.qs
        context['form_filters'] = filters.form
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product/update_products.html'
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('list-products')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product/delete_products.html'
    model = Product
    success_url = reverse_lazy('list-products')


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'product/detail_products.html'
    model = Product


def products_by_category(reques, category_id):
    products = Product.objects.filter(category=category_id)
    return render(request, 'products/products_by_category.html', {'products': products})


@login_required()
def delete_product_modal(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect('list_products')
