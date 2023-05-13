from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from core.models import Category,Project,State,Convocatory,Donation
from .forms import Edit_category_form,State_form,Project_form,Convocatory_form,Donation_form
from django.urls import reverse_lazy,reverse


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
            obj= obj.filter(project_id=card_id)
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
        category_id= self.request.GET.get("lang")
        if category_id:
            obj= obj.filter(category = category_id)
        return HttpResponse(render(request,'gallery.html',{'card':obj}))
     
class Project_view(View):
    def get(self,request):
        obj = Project.objects.all()
        obj1 = Project.objects.all()
        card_id= self.request.GET.get("lang")
        p = Project.objects.get(project_id = card_id)
        if card_id:
            obj= obj.filter(project_id=card_id)
            obj1=obj1.filter(category = p.category.category_id)
            obj1=obj1.exclude(project_id= card_id)
        return HttpResponse(render(request,'project.html',{'card':obj, 'card1':obj1})) 

#Convocatory CRUD
    

class Employee_convocatories(View):   
    def get(self, request):
        context={
            'convocatories': Convocatory.objects.all, 
            'active': 'convocatories',
        }
        return HttpResponse(render(request,'employee_views/convocatories_ehome.html',context))
    
class Save_convocatories(View):
    def get(self,request):


        context={
            'title' : 'Guardar convocatoria',
            'active': 'convocatories',
            'form': Convocatory_form(),
        }
        return HttpResponse(render(request,'employee_views/crud_convocatory_ehome.html',context))
    
    def post(self, request):
        form = Convocatory_form(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('core:econvocatories')  
        
        context = {
            'title': 'Guardar Convocatoria',
            'active': 'convocatories',
            'form': form,
        }
        return render(request, 'employee_views/crud_convocatory_ehome.html', context)
    
class Edit_convocatory(View):
    def get(self,request,convocatory_id):
        convocatory = Convocatory.objects.get(convocatory_id=convocatory_id)

        context={
            'title' : 'Editar Convocatoria',
            'convocatory':convocatory,
            'active': 'categories',
            'form': Convocatory_form(instance=convocatory),
        }
        return HttpResponse(render(request,'employee_views/crud_convocatory_ehome.html',context))
    
    def post(self, request, convocatory_id):
        convocatory = Convocatory.objects.get(convocatory_id=convocatory_id)
        form = Convocatory_form(request.POST, instance=convocatory)
        if form.is_valid():
            form.save()
            return redirect('core:econvocatories')  

        context = {
            'convocatory': convocatory,
            'active': 'categories',
            'form': form,
        }
        return render(request, 'employee_views/crud_convocatory_ehome.html', context)
    

class Delete_convocatory(View):
    def delete_convocatory(request,convocatory_id):
        convocatory = Convocatory.objects.get(convocatory_id=convocatory_id)
        convocatory.delete()

        return redirect('core:econvocatories')

#Category CRUD

class Employee_categories(View):   
    def get(self, request):
        context={
            'active': 'categories',
            'categories':Category.objects.all
        }
        return HttpResponse(render(request,'employee_views/categories_ehome.html',context))

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
            form.save()  
            return redirect('core:ecategories')  #
        
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
    

class Delete_category(View):
    def delete_category(request,category_id):
        category = Category.objects.get(category_id=category_id)
        category.delete()

        return redirect('core:ecategories')
    
#Project CRUD
class Employee_projects(View):   
    def get(self, request):
        context={
            'active': 'projects',
            'projects':Project.objects.all
        }
        return HttpResponse(render(request,'employee_views/projects_ehome.html',context))

    
class Save_project(View):
    def get(self,request):


        context={
            'title' : 'Guardar Proyecto',
            'active': 'projects',
            'form': Project_form(),

        }
        return HttpResponse(render(request,'employee_views/crud_project_ehome.html',context))
    
    def post(self, request):
        form = Project_form(request.POST,request.FILES)

        if form.is_valid():
            form.save()  
            return redirect('core:eprojects')  
    
        context = {
            'title': 'Guardar Proyecto',
            'active': 'projects',
            'form': form,
            'states':State.objects.all
        }
        return render(request, 'employee_views/crud_project_ehome.html', context)

class Edit_project(View):
    def get(self,request,project_id):
        print('entra get')
        project = Project.objects.get(project_id=project_id)

        context={
            'title' : 'Editar Proyecto',
            'project':project,
            'active': 'categories',
            'form': Project_form(instance=project),
        }
        return HttpResponse(render(request,'employee_views/crud_project_ehome.html',context))
    
    def post(self, request, project_id):
        project = Project.objects.get(project_id=project_id)
        form = Project_form(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('core:eprojects')  

        context = {
            'project': project,
            'active': 'projects',
            'form': form,
        }
        return render(request, 'employee_views/crud_project_ehome.html', context)

class Delete_project(View):
    def delete_project(request,project_id):
        project = Project.objects.get(project_id=project_id)
        project.delete()

        return redirect('core:eprojects')

#State CRUD
class Employee_states(View):   
    def get(self, request):
        context={
            'active': 'states',
            'states':State.objects.all
        }
        return HttpResponse(render(request,'employee_views/states_ehome.html',context))
    
class Save_state(View):
    def get(self,request):
        context={
            'title' : 'Guardar Estado',
            'active': 'states',
            'form': State_form,
        }
        return HttpResponse(render(request,'employee_views/crud_states_ehome.html',context))
    
    def post(self, request):
        form = State_form(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('core:estates')  
        
        context = {
            'title': 'Guardar Estado',
            'active': 'states',
            'form': form,
        }
        return render(request, 'employee_views/crud_states_ehome.html', context)
    
class Edit_state(View):
    def get(self,request,state_id):
        state = State.objects.get(state_id=state_id)

        context={
            'title' : 'Editar Estado',
            'state':state,
            'active': 'states',
            'form': State_form(instance=state),
        }
        return HttpResponse(render(request,'employee_views/crud_states_ehome.html',context))
    
    def post(self, request, state_id):
        state = State.objects.get(state_id=state_id)
        form = State_form(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('core:estates')  

        context = {
            'state': state,
            'active': 'states',
            'form': form,
        }
        return render(request, 'employee_views/crud_states_ehome.html', context)

class Delete_state(View):
    def delete_state(request,state_id):
        state = State.objects.get(state_id=state_id)
        state.delete()

        return redirect('core:estates')
    

class Donation_methods(View):
    def get(self,request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        obj = obj.filter(project_id=card_id)
        context={
            'form': Donation_form,
            'card': obj
        }
        return HttpResponse(render(request,'donation_methods.html',context))
    
    def post(self, request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        obj = obj.get(project_id=card_id)
        form = Donation_form(request.POST)
        if form.is_valid():
            donation = Donation()
            donation.payment_method = form.cleaned_data['payment_method']
            donation.amount = form.cleaned_data['amount']
            donation.user = request.user
            donation.project = obj
            donation.save()
            return redirect('core:successful_donation')  
        context={
            'form': Donation_form,
            'card': obj
        }
        return render(request, 'donation_methods.html', context)
    
    
class Successful_donation(View):
    def get(self,request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(project_id=card_id)

        return HttpResponse(render(request,'successful_donation.html',{'card':obj}))

class Convocatory_inscription(View):
    def get(self,request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(project_id=card_id)
        return HttpResponse(render(request,'convocatory_inscription.html',{'card':obj}))
