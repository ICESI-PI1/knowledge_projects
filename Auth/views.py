from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from core.models import Client
from . forms import ClientForm

# Create your views here.

def register(request):
    if (request.method == 'POST'):
        form = ClientForm(request.POST)

        if(request.POST['password_confirmation'] ==request.POST['password_confirmation']):
            """ 
            clien_data = request.POST.dict()
            clien_data.pop('password_confirmation')
            clien_data.pop('csrfmiddlewaretoken')
            client = Client(**clien_data)
            client.save() """
            # Recuperar los datos del formulario enviado por el usuario
            nit = request.POST.get('nit')
            name = request.POST.get('name')
            phoneNumber = request.POST.get('phoneNumber')
            adress = request.POST.get('adress')
            representativeName = request.POST.get('representativeName')
            phoneNumberRepresentative = request.POST.get('phoneNumberRepresentative')
            password = request.POST.get('password')

            # Crear un objeto de cliente con los datos proporcionados
            client = Client(nit=nit, name=name, phoneNumber=phoneNumber, adress=adress, representativeName=representativeName, phoneNumberRepresentative=phoneNumberRepresentative)
        
            # Establecer la contraseña del cliente utilizando el método set_password definido en el modelo Client
            client.set_password(password)

            # Guardar el objeto de cliente en la base de datos
            client.save()
            print('llega')
            return redirect('core:home')
            
        
        
        return render(request, 'register.html', {
            'form':ClientForm
        })
    else:
        
        return render(request, 'register.html', {
            'form': ClientForm
        })

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
