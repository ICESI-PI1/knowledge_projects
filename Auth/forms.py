from django import forms
from core.models import Client

class ClientForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirmar contraseña'}))
    class Meta:
        model = Client
        fields = [
            'nit',
            'name',
            'phoneNumber',
            'adress',
            'representativeName',
            'phoneNumberRepresentative',
            'password',
        ]
        widgets = {
            'nit': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nit'}),
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre'}),
            'phoneNumber':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Telefono'}),
            'adress':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Dirección'}),
            'representativeName':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre representante'}),
            'phoneNumberRepresentative':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Telefono representante'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Contraseña'}),
           
        }