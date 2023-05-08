from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Auth.decorators import client_required,employee_required
from django.views import View

from .models import Card

# Create your views here.

@login_required
@client_required
def home(request):
    obj = Card.objects.all()
    return render(request,'index.html',{'card':obj})

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