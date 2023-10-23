from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from category.forms import CategoryForm
from .models import Category


class CategoryCreateView(CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list-categories')
    success_message = 'Categoria {cname} a fost adaugata cu success.'
    permission_required = 'category.add_category'


class CategoryListView(ListView):
    template_name = 'category/list_categories.html'
    model = Category
    context_object_name = 'all_categories'


