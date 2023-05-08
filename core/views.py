from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from Auth.decorators import client_required,employee_required
from django.views import Viewfrom
from core.models import Category

# Create your views here.

@login_required
@client_required
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
        obj = Card.objects.all()
        card_id= self.request.GET.get("lang")
        if card_id:
            obj= obj.filter(id=card_id)
        return HttpResponse(render(request,'detailedinfo.html',{'project':obj,}))

class binnacle(View):
    def get(self,request):
      return render(request,'binnacle.html')
def home(request):
    obj = Card.objects.all()
    return render(request,'index.html',{'card':obj})