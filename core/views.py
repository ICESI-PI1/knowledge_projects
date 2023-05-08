from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Auth.decorators import client_required,employee_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from .models import Card

# Create your views here.

@login_required
@client_required
def home(request):
    obj = Card.objects.all()
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

@method_decorator(login_required, name='dispatch')
class Home_employee(TemplateView):
    template_name = "employee_home.html"
