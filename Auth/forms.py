from django import forms
from .models import Client,User
from django.contrib.auth.forms import AuthenticationForm



class User_login_form(AuthenticationForm):

     

    class Meta :
        model = User
        fields = [
            'username'
            'password'
        ]
        widgets = {
            'username' : forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','type':'text'})),
            'password': forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirmar contraseña'})),
        }


class Client_register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Contraseña'}))

    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirmar contraseña'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre'}))
    class Meta:
        model = Client
        
        fields = [
            'name',
            'phone_number',
            'address',
            'representative_name',
            'phone_number_representative'
        ]
        widgets = {
            'name':  forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Telefono'}),
            'address':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Dirección'}),
            'representative_name':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre representante'}),
            'phone_number_representative':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Telefono representante'}), 
        }

        



    


    