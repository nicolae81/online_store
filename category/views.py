from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from category.forms import CategoryForm, CategoryUpdateForm
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


class CategoryUpdateView(ListView):
    template_name = 'category/update_categories.html'
    model = Category
    form_class = CategoryUpdateForm
    success_url = reverse_lazy('list_categories')


class CategoryDeleteView(ListView):
    template_name = 'category/delete_category.html'
    model = Category
    form_class = CategoryUpdateForm
    success_url = reverse_lazy('list_categories')


class CategoryDetailView(ListView):
    template_name = 'category/details_category.html'
    model = Category

# @login_required()
# def delete_category_modal(request, pk):
#     Category.objects.filter(id=pk).delete()
#     return redirect('list_category')


