from django import forms

from .models import Category,State


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


class State_form(forms.ModelForm):
    class Meta :
        model = State
        fields = [
            'state_name',
            'description',
        ]
        widgets = {
            'state_name':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre:'}),
            'description':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Descripción:'}),
        }