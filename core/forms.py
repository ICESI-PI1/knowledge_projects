from django import forms

from .models import Category,State,Project, Donation


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


class Project_form(forms.ModelForm):
    class Meta :
        model = Project
        fields = [
            'project_name',
            'project_description',
            'result',
            'scope',
            'work_plan',
            'budget',
            'goal',
            'img',
            'state',
            'category',
        ]
        widgets = {

            'project_name':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre:'}),
            'project_description':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Descripción:'}),
            'result':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Resultado:'}),
            'scope':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Objetivo:'}),
            'work_plan':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Plan de trabajo:'}),
            'budget':forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Presupuesto:'}),
            'goal':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Meta:'}),
            'img':forms.FileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Imagen:'}),
            'state': forms.Select(attrs={'class': ''}),
            'category': forms.Select(attrs={'class': ''}),
            
        }

class Donation_form(forms.ModelForm):
    class Meta :
        model = Donation
        fields = [
            'payment_method',
            'amount',
        ]
        widgets = {
            'payment_method':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Método de pago:'}),
            'amount':forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Monto:'}),
        }