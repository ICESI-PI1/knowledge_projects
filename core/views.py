from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Auth.decorators import client_required,employee_required
from django.views import View


from .models import Card

# Create your views here.

# @login_required
# @client_required

class Home(View):
    def get(self,request):
        obj = Card.objects.all()
        return HttpResponse(render(request,'gallery.html',{'card':obj}))
    
class Project(View):
    def get(self,request):
        obj = Card.objects.all()
        obj1 = Card.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'project.html',{'card':obj, 'card1':obj1})) 
    
class Convocatory(View):
    def get(self, request):
        obj = Card.objects.all()
        return HttpResponse(render(request,'convocatory.html',{'card':obj}))
    
class Inscription(View):
     def get(self,request):
        obj = Card.objects.all()
        obj1 = Card.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'inscription.html',{'card':obj, 'card1':obj1})) 