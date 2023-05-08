
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate, login 
from .forms import User_login_form,Client_register_form
from django.views.generic import CreateView
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView




# Create your views here.
class User_login_view(LoginView):
    def user_login(request):
        if request.method == 'POST':
            # Obtén los datos del formulario de inicio de sesión enviado por el usuario
            username = request.POST['username']
            password = request.POST['password']

            
            try:
                user = User.objects.get(username=username)
                if user.is_client:
                    if (user.check_password(password)):
                        login(request, user)
                        return redirect('core:home')

                elif user.is_employee:
                    print('empleado')
                    print('var ',password)
                    print('pass ',user.password)
                    if(user.password==password):
                        print('entra')
                        return redirect('core:ehome')

                else:
                    return None
            except User.DoesNotExist:
                return render(request, 'login.html', {'form': User_login_form})
        else:
            return render(request, 'login.html', {'form': User_login_form})






        
    









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
    
def detailed_info(request):
    return render(request,'detailedinfo.html')

def bitacora(request):
    return render(request,'bitacora.html')

