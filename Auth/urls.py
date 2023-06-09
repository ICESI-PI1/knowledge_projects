from django.urls import path
from .views import User_login_view,Client_register_view
from Auth import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'auth'

urlpatterns = [
    path('register/',Client_register_view.as_view(),name='register'),
    path('login/',User_login_view.as_view(),name='login'),
    path('logout/',views.logout_request,name='logout'),
]