import django_filters
from django import forms
from product.models import Product


class ProductFilter(django_filters.FilterSet):

    common_attrs = {
        'lookup_expr': 'icontains',
        'widget': forms.TextInput(attrs={'class': 'form-control'}),
    }
    name = django_filters.CharFilter(
        label='Title',
        **common_attrs
    )
    price = django_filters.NumberFilter(
        label='Price',
        **common_attrs
    )
    created_at = django_filters.DateTimeFilter(
        label='Created At',
        **common_attrs
    )
    updated_at = django_filters.DateTimeFilter(
        label='Updated At',
        **common_attrs
    )
    in_stock = django_filters.BooleanFilter(
        label='In Stock',
        **common_attrs
    )
    is_active = django_filters.BooleanFilter(
        label='Is Active',
        **common_attrs
    )

    class Meta:
        model = Product
        fields = ['name', 'price']



    # Long Way!!!!! #
    # name = django_filters.CharFilter(
    #     lookup_expr='icontains',
    #     label='Title',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # price = django_filters.NumberFilter(
    #     lookup_expr='icontains',
    #     label='Price',
    #     widget=forms.NumberInput(attrs={'class': 'form-control'})
    # )
    # created_at = django_filters.DateTimeFilter(
    #     lookup_expr='icontains',
    #     label='Created At',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # updated_at = django_filters.DateTimeFilter(
    #     lookup_expr='icontains',
    #     label='Updated At',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # in_stock = django_filters.BooleanFilter(
    #     lookup_expr='icontains',
    #     label='In Stock',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    # is_active = django_filters.BooleanFilter(
    #     lookup_expr='icontains',
    #     label='Is Active',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    #  )


