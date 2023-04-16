from django.shortcuts import render
from django.http import HttpResponse

from .models import Card

# Create your views here.


def home(request):
    obj = Card.objects.all()
    return render(request,'index.html',{'card':obj})