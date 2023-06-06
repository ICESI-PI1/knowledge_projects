from django import forms
from .models import Client,Employee,User
from django.contrib.auth.forms import AuthenticationForm



class User_login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': ''}),required=True)
    class Meta :
        model = User
        fields = [
        ]
        widgets = {
        }

class Client_register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': ''}),required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': ' '}),required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),required=True)
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
            'name':  forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
            'phone_number':forms.NumberInput(attrs={'class': 'input', 'placeholder': ''}),
            'address':forms.TextInput(attrs={'class': 'input', 'placeholder': ''}),
            'representative_name':forms.TextInput(attrs={'class': 'input', 'placeholder': ' '}),
            'phone_number_representative':forms.NumberInput(attrs={'class': 'input', 'placeholder': ''}),
        }


class Employee_register_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Contraseña'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirmar contraseña'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Cedula'}))

    class Meta:
        model = Employee
        
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'img'

        ]
        widgets = {
            'first_name':  forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Apellido'}),
            'birth_date': forms.DateInput(attrs={'type': 'date','class': 'form-control', 'placeholder': 'Fecha de nacimiento:'}),
            'img':forms.FileInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Imagen:'}),
        
        }


class Employee_change_password(forms.ModelForm):
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Contraseña'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Contraseña'}))

    new_password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        
        fields = [
            'password'

        ]
        widgets = {

        }


class Employee_edit_form(forms.ModelForm):


    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Cedula', 'readonly': 'readonly'})
    )

    class Meta:
        model = Employee
        
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'img'

        ]
        widgets = {
            'first_name':  forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Apellido'}),
            'birth_date': forms.DateInput(attrs={'type': 'date','class': 'form-control', 'placeholder': 'Fecha de nacimiento:'}),
            'img':forms.FileInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Imagen:'}),
        
        }

        



    


    