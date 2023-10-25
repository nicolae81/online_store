
import django_filters
from django import forms
    
from category.models import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # created_at = django_filters.DateTimeFilter(
    #     lookup_expr='icontains',
    #     label='Created At',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    #
    # updated_at = django_filters.DateTimeFilter(
    #     lookup_expr='icontains',
    #     label='Updated At',
    #     widget=forms.TextInput(attrs={'class': 'form-control'})

    class Meta:
        model = Category
        fields = '__all__'




    # name = django_filters.CharFilter(lookup_expr='icontains', label='Name',
    #                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    # list_category = [(category.id, f'{category.name}') for category in
    #                     Category.objects.filter(active=True)]
    # # print(list_category)
    #
    # def filter_category_choices(queryset, name, value):
    #     return [(category.id, category.name) for category in queryset]
    #
    # category = django_filters.ChoiceFilter(fild_name='category', choices=filter_category_choices,
    #                                       widget=forms.Select(attrs={'class': 'form-select'}))
    #
    # start_date_gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', widget=forms.DateInput(
    #     attrs={'class': 'form-control', 'type': 'date'}))
    #
    # start_date_lte = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', widget=forms.DateInput(
    #     attrs={'class': 'form-control', 'type': 'date'}))

    # class Meta:
    #     model = Category
    #     field = '__all__'
        # field = ['name', 'category', 'start_date_gte', 'start_date_lte']

