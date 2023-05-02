from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Auth.decorators import client_required,employee_required


from .models import Card

# Create your views here.

@login_required
@client_required
def home(request):
    obj = Card.objects.all()
    return render(request,'index.html',{'card':obj})