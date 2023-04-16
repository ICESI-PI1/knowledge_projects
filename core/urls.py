
from django.urls import include, path

from core import views

app_name = 'core'

urlpatterns = [
    path('home/', views.index, name = 'home'),
]