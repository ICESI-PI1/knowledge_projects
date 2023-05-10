from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from Auth.decorators import client_required,employee_required
from core.models import Category
from core.models import Project

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
        return HttpResponse(render(request,'employee_home_view.html'))

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


class Donation_methods(View):
    def get(self,request):
        obj = Card.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'donation_methods.html',{'card':obj}))
    
class Successful_donation(View):
    def get(self,request):
        obj = Card.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)

        return HttpResponse(render(request,'successful_donation.html',{'card':obj}))
        

