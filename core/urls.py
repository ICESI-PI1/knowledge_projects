
from django.urls import include, path
from .views import Home_employee

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name ='home'),
    path('base/',views.base,name="base"),
    path('ehome/',Home_employee.as_view(),name='ehome')
]