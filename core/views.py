from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from Auth.decorators import client_required,employee_required


from .models import Card

# Create your views here.

class Home_view(View):   
    def get(self, request):
        
        username = None
        if request.user.is_authenticated:
            username = request.user.username

        context = {"username" : 'Hola, ' + username.capitalize(),}

        return HttpResponse(render(request,'home_view.html',context))