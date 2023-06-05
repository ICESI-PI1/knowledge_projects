from django import forms
from .models import Client,Employee,User
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


class Client_register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Contraseña'}))

    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirmar contraseña'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nit'}))
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

        



    


    