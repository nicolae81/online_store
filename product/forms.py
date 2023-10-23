import self
from django import forms
from django.forms import TextInput, Textarea, DateInput, Select
from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'category': Select(attrs={'class': 'form-select'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'in_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'updated_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        get_description = cleaned_data['description']
        if len(get_description) < 5:
            msg = 'Trebuie sa adaugi minim 5 caractere'
            self._errors['description'] = self.error_class([msg])

            return cleaned_data


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'category': Select(attrs={'class': 'form-select'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'in_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'updated_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
