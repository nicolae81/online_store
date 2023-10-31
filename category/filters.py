import django_filters
from django import forms

from category.models import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Category
        fields = '__all__'
