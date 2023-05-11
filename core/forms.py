from django import forms

from .models import Category


class Edit_category_form(forms.ModelForm):
    class Meta :
        model = Category
        fields = [
            'category_name',
            'icon_src',
            'description',
        ]
        widgets = {
            'category_name':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre:'}),
            'icon_src':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ruta icono:'}),
            'description':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Descripción:'}),
        }