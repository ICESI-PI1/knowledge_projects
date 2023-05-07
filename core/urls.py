from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('home/', views.Home_view.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()