from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from manage_users.models import History
from product.models import Product
from product.forms import ProductForm
from datetime import datetime


class ProductCreateView(CreateView):
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

            History.objects.create(text=history_text, created_at=datetime.now(), updated_at=datetime.now(), product=new_product)
        return redirect('list_products')


class ProductListView(ListView):
    template_name = 'product/list_products.html'
    model = Product
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


