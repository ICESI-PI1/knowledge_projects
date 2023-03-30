from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.

def register(request):
    if request.method == 'GET':
        form = UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'Auth/register.html',context)

