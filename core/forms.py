from django import forms
from .models import Category,State,Project,Convocatory,Donation, Suggestion, Comments



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
            'convocatory',
        ]
        widgets = {

            'project_name':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Nombre:'}),
            'project_description':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Descripción:'}),
            'result':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Resultado:'}),
            'scope':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Objetivo:'}),
            'work_plan':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Plan de trabajo:'}),
            'budget':forms.NumberInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Presupuesto:'}),
            'goal':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Meta:'}),
            'img':forms.FileInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Imagen:'}),
            'state': forms.Select(attrs={'class': ''}),
            'category': forms.Select(attrs={'class': ''}),
            'convocatory': forms.Select(attrs={'class': 'form-control mb-1', 'placeholder': 'Convocatoria:'}),
            
        }





class Convocatory_form(forms.ModelForm):
    class Meta :
        model = Convocatory
        fields = [
            'convocatory_name',
            'start_date',
            'closing_date',
        ]
        widgets = {
            'convocatory_name':forms.TextInput(attrs={'size': 30,'class': 'form-control', 'placeholder': 'Nombre:'}),
            'start_date': forms.DateInput(attrs={'type': 'date','class': 'form-control', 'placeholder': 'Fecha inicio:'}),
            'closing_date': forms.DateInput(attrs={'type': 'date','class': 'form-control ', 'placeholder': 'Fecha Fin:'}),
        }

class Suggestion_form(forms.ModelForm):
     class Meta :
        model = Suggestion
        fields = [
            'suggestion_name',
            'suggestion_description',
            'suggestion_work_plan',
            'suggestion_budget',
        ]
        widgets = {
            'suggestion_name':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Nombre'}),
            'suggestion_description':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Descripción'}),
            'suggestion_work_plan':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Plan de trabajo'}),
            'suggestion_budget':forms.NumberInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Presupuesto'}),
        }

class Comment_form(forms.ModelForm):
     class Meta :
        model = Comments
        fields = [
            'text',
        ]
        widgets = {
            'text':forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Comenta'}),
        }