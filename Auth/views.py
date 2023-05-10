from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from .forms import User_login_form,Client_register_form
from django.views.generic import CreateView
from .models import User
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
        # Crear el usuaraio
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            is_client=True
        )

        client = form.save(commit=False)
        client.user = user
        client.save()

        

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

