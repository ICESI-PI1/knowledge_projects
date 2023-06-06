from django.contrib import admin
from .models import State,Category,Project,Convocatory
from .models import Binnacle,Log,Donation, Suggestion, Comments, Beneficiary


# Register your models here.
admin.site.register(State)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Convocatory)
admin.site.register(Binnacle)
admin.site.register(Log)
admin.site.register(Donation)
admin.site.register(Suggestion)
admin.site.register(Comments)
admin.site.register(Beneficiary)