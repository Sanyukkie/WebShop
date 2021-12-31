from django import forms
from django.forms import ModelForm
from .models import Product, ProductAttribute


# Create a Product form

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'detail', 'specs', 'category', 'brand')

        labels = {
            'title': '',
            'detail': '',
            'specs': '',
            'category': '',
            'brand': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'detail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Details'}),
            'specs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specifications'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
        }


class AttributeForm(ModelForm):
    class Meta:
        model = ProductAttribute
        fields = ('product', 'color', 'price', 'image')
        labels = {
            'product': 'Choose your product',
            'color': 'Select product color',
            'price': 'Price:',
            'image': 'Select your products image',
        }

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }




