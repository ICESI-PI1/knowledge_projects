from django.contrib import admin
from .models import Client,Project,Employee,Rol
from .models import Card 

# Register your models here.
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Rol)

admin.site.register(Card)