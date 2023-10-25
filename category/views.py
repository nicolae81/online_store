from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from category.forms import CategoryForm, CategoryUpdateForm
from .filters import CategoryFilter
from .models import Category, History


class CategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list-categories')
    success_message = 'Categoria {cname} a fost adaugata cu success.'
    permission_required = 'category.add_category'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(cname=self.object.name)

    def form_valid(self, form):
        if form.is_valid():
            new_category = form.save()
            history_text = f'{new_category.name} was successfully created on {datetime.now()}'
            History.objects.create(text=history_text, created_at=datetime.now(),)
        return redirect('list-categories')


class CategoryListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'category/list_categories.html'
    model = Category
    context_object_name = 'all_categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_all_categories = Category.objects.all()
        filters = CategoryFilter(self.request.GET, queryset=get_all_categories)
        context['all_categories'] = filters.qs
        context['form_filters'] = filters.form
        return context


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'category/update_categories.html'
    model = Category
    form_class = CategoryUpdateForm
    success_url = reverse_lazy('list-categories')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = reverse_lazy('list-categories')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'category/details_category.html'
    model = Category

@login_required()
def delete_category_modal(request, pk):
    Category.objects.filter(id=pk).delete()
    return redirect('list-categories')


