from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('detailedinfo/', views.detailed_info, name='detailedinfo'),
     path('bitacora/', views.bitacora, name='bitacora'),
] 
