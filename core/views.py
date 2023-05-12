from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from Auth.decorators import client_required,employee_required
from core.models import Category
from core.models import Project
from .forms import Edit_category_form

# Create your views here.

class Home_view(View):   
    def get(self, request):
        
        username = None
        if request.user.is_authenticated:
            username = request.user.username
            context = {"username" : 'Hola, ' + username.capitalize(),}
            return HttpResponse(render(request,'home_view.html',context))
        
        return HttpResponse(render(request,'home_view.html'))

class Categories_view(View):   
    def get(self, request):
        data = Category.objects.all()
        context={
        'data': data
        }
        return HttpResponse(render(request,'categories_view.html',context))
    
class detailed_info(View):
    def get(self,request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'detailedinfo.html',{'card':obj,}))

class binnacle(View):
    def get(self,request):
      return render(request,'binnacle.html')


class Home_view_employee(View):   
    def get(self, request):
        context={
            'active': 'dashboard'
        }
        return HttpResponse(render(request,'employee_home_view.html',context))
    
class Employee_categories(View):   
    def get(self, request):
        context={
            'active': 'categories',
            'categories':Category.objects.all
        }
        return HttpResponse(render(request,'employee_views/categories_ehome.html',context))
    
class Employee_projects(View):   
    def get(self, request):
        context={
            'active': 'projects',
        }
        return HttpResponse(render(request,'projects_ehome.html',context))
    

class Employee_convocatories(View):   
    def get(self, request):
        context={
            'active': 'convocatories',
        }
        return HttpResponse(render(request,'convocatories_ehome.html',context))
    
class Employee_clients(View):   
    def get(self, request):
        context={
            'active': 'clients',
        }
        return HttpResponse(render(request,'clients_ehome.html',context))
    
class Employee_tools(View):   
    def get(self, request):
        context={
            'active': 'tools',
        }
        return HttpResponse(render(request,'tools_ehome.html',context))
    
class Gallery(View):
    def get(self,request):
        obj = Project.objects.all()
        return HttpResponse(render(request,'gallery.html',{'card':obj}))
    
class Project_view(View):
    def get(self,request):
        obj = Project.objects.all()
        obj1 = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'project.html',{'card':obj, 'card1':obj1})) 
    
class Convocatory(View):
    def get(self, request):
        obj = Project.objects.all()
        return HttpResponse(render(request,'convocatory.html',{'card':obj}))
    
class Inscription(View):
     def get(self,request):
        obj = Project.objects.all()
        obj1 = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'inscription.html',{'card':obj, 'card1':obj1})) 

class Delete_category(View):
    def deleteCategory(request,category_id):
        category = Category.objects.get(category_id=category_id)
        category.delete()

        return redirect('core:ecategories')

class Save_Category(View):
    def get(self,request):


        context={
            'title' : 'Guardar Categoría',
            'active': 'categories',
            'form': Edit_category_form(),
        }
        return HttpResponse(render(request,'employee_views/edit_category.html',context))
    
    def post(self, request):
        form = Edit_category_form(request.POST)
        if form.is_valid():
            form.save()  # Guardar la categoría en la base de datos
            return redirect('core:ecategories')  # Redirigir a la vista deseada después de guardar
        

        # Si el formulario no es válido, volver a renderizar el formulario con los errores
        context = {
            'title': 'Guardar Categoría',
            'active': 'categories',
            'form': form,
        }
        return render(request, 'employee_views/edit_category.html', context)
    
        



    
class Edit_category(View):
    def get(self,request,category_id):
        category = Category.objects.get(category_id=category_id)

        context={
            'title' : 'Editar Categoría',
            'category':category,
            'active': 'categories',
            'form': Edit_category_form(instance=category),
        }
        return HttpResponse(render(request,'employee_views/edit_category.html',context))
    
    def post(self, request, category_id):
        category = Category.objects.get(category_id=category_id)
        form = Edit_category_form(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('core:ecategories')  

        context = {
            'category': category,
            'active': 'categories',
            'form': form,
        }
        return render(request, 'employee_views/edit_category.html', context)

class Donation_methods(View):
    def get(self,request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'donation_methods.html',{'card':obj}))
    
class Successful_donation(View):
    def get(self,request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)

        return HttpResponse(render(request,'successful_donation.html',{'card':obj}))
        
