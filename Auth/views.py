from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout 
from .forms import User_login_form,Client_register_form
from django.views.generic import CreateView
from .models import User,Client
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView




# Create your views here.
class User_login_view(LoginView):

    form_class = User_login_form
    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_client:
                return reverse('core:home')
            elif user.is_employee:
                return reverse('core:employee_home')
        else:
            return reverse('login')



class Client_register_view(CreateView):
    
    model = User
    form_class = Client_register_form
    template_name = 'register.html'
    success_url = reverse_lazy('core:home')


    def form_valid(self, form):
        user = User()
        user.username = form.cleaned_data['username']
        user.password = form.cleaned_data['password']
        user.is_client = True  
        user.is_employee = False  
        user.save()
   
        client = Client.objects.create(
            user=user,
            name=form.cleaned_data['name'],
            phone_number=form.cleaned_data['phone_number'],
            address=form.cleaned_data['address'],
            representative_name=form.cleaned_data['representative_name'],
            phone_number_representative=form.cleaned_data['phone_number_representative']
        )

        
        order = form.save(commit=False) 
        order.user = user 
        order.save() 

        return super().form_valid(form)




def user_login(request):

    if(request.method == 'POST'):
        nit = request.POST['nit']
        password = request.POST['password']
        user = authenticate(request, nit=nit, password=password)
 
        if user is not None:
            print('none')
            login(request, user)
            return redirect('core:home')
        else:
            print('is none')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout_request(request):
    logout(request)
    return redirect('core:home')