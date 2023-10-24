from category import forms
import django_filters


class CategoryFilters(django_filters.FilterSet):
    name = django_filters.CharField(lookup_expr='icontains', label='First name',
                                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    created_at = django_filters.DateTimeField(lookup_expr='icontains', label='Created At',
                                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    updated_at = django_filters.DateTimeField(lookup_expr='icontains', label='Updated At',
                                           widget=forms.TextInput(attrs={'class': 'form-control'}))
