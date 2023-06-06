from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from core.models import Category,Project,State,Convocatory,Donation, Suggestion, Comments, Beneficiary
from Auth.forms import Employee_register_form,Employee_edit_form,Employee_change_password
from .forms import Edit_category_form,State_form,Project_form,Convocatory_form,Suggestion_form, Comment_form,Beneficiary_form
from Auth.models import Client,Employee,User
from django.urls import reverse
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator





import stripe


SECRET_KEY = "sk_test_51NFiTZLtn7velaE9MPVYsbbL1R9yZ57rWnyR8RLW9mE8SvoFy9Unvf0WQq81vugXUj2ZPH8ccfBIzYJ3GPKPrG6d00nalYbtJf"

stripe.api_key=SECRET_KEY


# Create your views here.


class Project_view(View):
    def get(self,request):
        obj = Project.objects.all()
        obj1 = Project.objects.all()
        card_id= self.request.GET.get("lang")
        p = Project.objects.get(project_id = card_id)
        convocatory = None
        donations = Donation.objects.all()

        if (donations):
            donations = donations.get(project = card_id)
        if (p.convocatory):
            convocatory = p.convocatory

        if card_id:
            obj= obj.filter(project_id=card_id)[0]
            obj1=obj1.filter(category = p.category.category_id)
            obj1=obj1.exclude(project_id= card_id)
        return HttpResponse(render(request,'project.html',{'project':obj, 'related':obj1, 'don':donations, 'conv': convocatory})) 
class Donation_methods(View):
    def get(self,request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        obj = obj.filter(project_id=card_id)
        context={
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
    
@method_decorator(login_required, name='dispatch')
class Stripe_donation(View):
    def get(self, request,project_id):

        project = Project.objects.get(project_id=project_id)
        amount = project.budget

        context={
            'project':project,
            'amount': amount,
        }

        return HttpResponse(render(request,'donation_views/stripe_donation_view.html',context))

    def post(self, request,project_id):
        token = request.POST.get('stripeToken')
        email = request.POST.get('email')

  

        project = Project.objects.get(project_id=project_id)  
        amount = project.budget

        try:

            charge = stripe.Charge.create(
                amount=amount*100,  # Monto en centavos de la moneda especificada
                currency='usd',  # Moneda
                source=token,
                description='Ejemplo de pago con Stripe',
            )



            context={
                'project':project,
            }

            print('aqui')

            donation = Donation()
            donation.amount = project.budget
            donation.user = request.user
            donation.project = project
            donation.save()


            return HttpResponse(render(request,'successful_donation.html',context))

        
        except stripe.error.CardError as e:
            error = e.error.message
            context={
                'project':project,
                'amount': amount,
                'error':error,
            }

            return HttpResponse(render(request,'donation_views/stripe_donation_view.html',context))



class Home_view(View):   
    def get(self, request):
        username = None
        if request.user.is_authenticated:
            username = request.user.username
            context = {"username" : 'Hola, ' + username,}
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
            obj= obj.filter(project_id=card_id)[0]
        comment = Comments.objects.filter(project = card_id)
        donations = Donation.objects.filter(project = card_id)

        context={
            'form': Comment_form,
            'project':obj,
            'com':comment,
            'don':donations
        }
        return HttpResponse(render(request,'detailedinfo.html',context))
    
    def post(self, request):
        obj = Project.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(project_id=card_id)[0]
        comment = Comments.objects.filter(project = card_id)
        donations = Donation.objects.filter(project = card_id)

        context={
            'form': Comment_form,
            'project':obj,
            'com':comment,
            'don':donations
        }
        
        form = Comment_form(request.POST)
        if form.is_valid():
            comment = Comments()
            comment.author = request.user
            comment.text = form.cleaned_data['text']
            comment.project = obj
            comment.save()

        return render(request, 'detailedinfo.html', context)

class binnacle(View):
    def get(self,request):
      return render(request,'binnacle.html')


class Home_view_employee(View):   
    def get(self, request):
        n_projects =Project.objects.count()
        n_donations =Donation.objects.count()
        n_convocatories =Convocatory.objects.count()
        n_clients = Client.objects.count()

        context={
            'active': 'dashboard',
            'n_projects':n_projects,
            'n_donations':n_donations,
            'n_convocatories':n_convocatories,
            'n_clients':n_clients,


        }
        return HttpResponse(render(request,'employee_views/employee_home_view.html',context))
    
    
class Employee_clients(View):   
    def get(self, request):
        context={
            'active': 'clients',
        }
        return HttpResponse(render(request,'clients_ehome.html',context))
    
class Employee_tools(View):   
    def get(self, request):
        employees = Employee.objects.all()

        context={
            'active': 'tools',
            'user':request.user,
            'employees':employees,
        }
        return HttpResponse(render(request,'tools_ehome.html',context))
    
class Gallery(View):
     def get(self,request):
        obj = Project.objects.all()
        category_id= self.request.GET.get("lang")
        if category_id:
            obj= obj.filter(category = category_id)
        return HttpResponse(render(request,'gallery.html',{'card':obj}))
     


class Employee_tools(View):   
    def get(self, request):
        employees = Employee.objects.all()
        context={
            'active': 'tools',
            'user':request.user,
            'employees':employees,
        }
        return HttpResponse(render(request,'employee_views/tools_ehome.html',context))

#Employee CRUD
@method_decorator(login_required, name='dispatch')
class Save_employee(View):
    def get(self,request):
        context={
            'title' : 'Guardar empleado',
            'active': 'tools',
            'form': Employee_register_form(),
        }
        return HttpResponse(render(request,'employee_views/crud_employee_ehome.html',context))
    
    def post(self, request):
        form = Employee_register_form(request.POST,request.FILES)
        if form.is_valid():

            user = User()
            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data['password']
            user.is_client = False  
            user.is_employee = True  
            user.save()
            
            employee = Employee.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                birth_date=form.cleaned_data['birth_date'],
                img=form.cleaned_data['img']    
            )

            order = form.save(commit=False) 
            order.user = user 
            order.save() 

            return redirect('core:etools')
        
        context = {
            'title': 'Guardar Empleados',
            'active': 'tools',
            'form': form,
        }
        return render(request, 'employee_views/crud_employee_ehome.html', context)
    
class Delete_employe(View):
    def delete_employee(request,username):
        user = User.objects.get(username=username)
        user.delete()
        return redirect('core:etools')
    
class Change_employee_password(View):
    def get(self,request,username):


        context={
            'user':username,
            'form':Employee_change_password(),
            'active': 'tools',

        }
        
        return HttpResponse(render(request,'employee_views/change_password_employee_ehome.html',context))
    
    def post(self, request,username):
        form = Employee_change_password(request.POST)
        if form.is_valid():



            password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']
            new_password_confirmation = form.cleaned_data['new_password_confirmation']
            user = User.objects.get(username=username)

            if check_password(password, user.password):
                if(new_password==new_password_confirmation):

                    user.set_password(make_password(new_password))
                    user.save()
                    form.save()
                else:
                    context={
                        'user':username,
                        'form':Employee_change_password(),
                        'active': 'tools',

                    }
        
                    return HttpResponse(render(request,'employee_views/change_password_employee_ehome.html',context))
            else:
                context={
                    'user':username,
                    'form':Employee_change_password(),
                    'active': 'tools',

                }
        
                return HttpResponse(render(request,'employee_views/change_password_employee_ehome.html',context))

    

            return redirect(reverse('core:edit_employee_ehome', kwargs={'username': user.username}))
        
        context={
            'user':username,
            'form':Employee_change_password(),
        }
        
        return HttpResponse(render(request,'employee_views/change_password_employee_ehome.html',context))



class Edit_employee(View):
    def get(self,request,username):

        user = User.objects.get(username=username)
        employee = Employee.objects.get(user=user)

        form = Employee_edit_form(instance=employee)
        form.fields['username'].initial = username
        form.fields['img'].initial = employee.img 

        context={
            'title' : 'Editar Empleado',
            'active': 'tools',
            'form': form,
            'img': employee.img, 
            'username':employee.user.username,
        }
        return HttpResponse(render(request,'employee_views/edit_employee_ehome.html',context))
    
    def post(self, request, username):

        user = User.objects.get(username=username)
        employee = Employee.objects.get(user=user)

        form = Employee_edit_form(request.POST, request.FILES, instance=employee)

        if form.is_valid():

            employee = Employee.objects.get(user=user)
            form = Employee_edit_form(request.POST, request.FILES, instance=employee)
            if form.is_valid():
                form.save()
                return redirect('core:etools')  


        form.fields['username'].initial = username
        form.fields['img'].initial = employee.img 

        context={
            'title' : 'Editar Empleado',
            'active': 'tools',
            'form': form,
            'img': employee.img, 
        }

        return render(request, 'employee_views/edit_employee_ehome.html', context)

#Convocatory CRUD 
@method_decorator(login_required, name='dispatch')
class Employee_convocatories(View):   
    def get(self, request):
        context={
            'convocatories': Convocatory.objects.all, 
            'active': 'convocatories',
        }
        return HttpResponse(render(request,'employee_views/convocatories_ehome.html',context))

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
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
    
@method_decorator(login_required, name='dispatch')

class Delete_convocatory(View):
    def delete_convocatory(request,convocatory_id):
        convocatory = Convocatory.objects.get(convocatory_id=convocatory_id)
        convocatory.delete()
        return redirect('core:econvocatories')

#Category CRUD
@method_decorator(login_required, name='dispatch')
class Employee_categories(View):   
    def get(self, request):
        context={
            'active': 'categories',
            'categories':Category.objects.all
        }
        return HttpResponse(render(request,'employee_views/categories_ehome.html',context))
@method_decorator(login_required, name='dispatch')
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
            return redirect('core:ecategories')  
        
        context = {
            'title': 'Guardar Categoría',
            'active': 'categories',
            'form': form,
        }
        return render(request, 'employee_views/edit_category.html', context)


@method_decorator(login_required, name='dispatch') 
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
    
@method_decorator(login_required, name='dispatch')

class Delete_category(View):
    def delete_category(request,category_id):
        category = Category.objects.get(category_id=category_id)
        category.delete()

        return redirect('core:ecategories')
#Beneficiary CRUd
@method_decorator(login_required, name='dispatch')
class Edit_beneficiaries(View):
    def get(self, request,beneficiary_id):

        val = self.request.GET.get("lang")

        setval = self.request.GET.get("lang")
        
        beneficiaries = Beneficiary.objects.get(beneficiary_id=beneficiary_id)
        beneficiaries.is_approved = setval
        beneficiaries.save()

        all_beneficiaries = Beneficiary.objects.all() 


        if (val):
            all_beneficiaries = all_beneficiaries.filter(is_approved=val)
        
        
        context={
            'active': 'beneficiaries',
            'beneficiaries':all_beneficiaries,
        }

        return HttpResponse(render(request,'employee_views/beneficiaries_ehome.html',context))

        


        

class Employee_beneficiaries(View):  
    def get(self, request):

        val = self.request.GET.get("lang")
        
        beneficiaries = Beneficiary.objects.all() 


        if (val):
            beneficiaries = beneficiaries.filter(is_approved=val)
        
            



        context={
            'active': 'beneficiaries',
            'beneficiaries':beneficiaries,
        }
        return HttpResponse(render(request,'employee_views/beneficiaries_ehome.html',context))

#Project CRUD
@method_decorator(login_required, name='dispatch')
class Employee_projects(View):   
    def get(self, request):
        context={
            'active': 'projects',
            'projects':Project.objects.all
        }
        return HttpResponse(render(request,'employee_views/projects_ehome.html',context))

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class Edit_project(View):
    def get(self,request,project_id):
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

@method_decorator(login_required, name='dispatch')
class Delete_project(View):
    def delete_project(request,project_id):
        project = Project.objects.get(project_id=project_id)
        project.delete()

        return redirect('core:eprojects')

#State CRUD
@method_decorator(login_required, name='dispatch')
class Employee_states(View):   
    def get(self, request):
        context={
            'active': 'states',
            'states':State.objects.all
        }
        return HttpResponse(render(request,'employee_views/states_ehome.html',context))

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class Delete_state(View):
    def delete_state(request,state_id):
        state = State.objects.get(state_id=state_id)
        state.delete()

        return redirect('core:estates')
    

    
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
        context={
            'form': Beneficiary_form,
            'card':obj,
        }
        return HttpResponse(render(request,'convocatory_inscription.html',context))
    
    def post(self, request):
        form = Beneficiary_form(request.POST)
        if form.is_valid():
            beneficiary = Beneficiary()
            user = request.user
            client = Client.objects.all()
            client = client.get(user=user)
            beneficiary.user = client
            beneficiary.email = form.cleaned_data['email']
            beneficiary.phone_number = client.phone_number
            beneficiary.representative_name = client.representative_name
            beneficiary.phone_number_representative = client.phone_number_representative
            beneficiary.save()
            return redirect('core:home')  
        context={
            'form': Beneficiary_form,
        }
        return render(request, 'convocatory_inscription.html', context)

class Suggestion_view(View):
    def get(self,request):
        context={
            'form': Suggestion_form,
        }
        return HttpResponse(render(request,'suggestions.html',context))
    
    def post(self, request):
        form = Suggestion_form(request.POST)
        if form.is_valid():
            suggestion = Suggestion()
            suggestion.suggestion_name = form.cleaned_data['suggestion_name']
            suggestion.suggestion_description = form.cleaned_data['suggestion_description']
            suggestion.suggestion_work_plan = form.cleaned_data['suggestion_work_plan']
            suggestion.suggestion_budget = form.cleaned_data['suggestion_budget']
            suggestion.save()
            return redirect('core:home')  
        context={
            'form': Suggestion_form,
        }
        return render(request, 'suggestions.html', context)