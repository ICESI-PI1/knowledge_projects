
from django.urls import include, path

from core import views
from core.views import Project
from core.views import Home
from core.views import Convocatory
from core.views import Inscription

app_name = 'core'

urlpatterns = [
    path('home/', Home.as_view(), name ='home'),
    path('project/', Project.as_view(), name ='project'),
    path('convocatory/', Convocatory.as_view(), name='convocatory'),
    path('inscription/', Inscription.as_view(), name='inscription'),
]