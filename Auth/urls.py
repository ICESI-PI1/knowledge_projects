from django.urls import path
from .views import User_login_view,Client_register_view
from Auth import views

 
urlpatterns = [
    path('register/',Client_register_view.as_view(),name='register'),
    path('',User_login_view.as_view(),name='login'),
] 
