from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views
from core.views import detailed_info
from core.views import binnacle
from core.views import Project_view
from core.views import Gallery
from core.views import Convocatory
from core.views import Inscription
app_name = 'core'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('home/', views.Home_view.as_view(), name='home'),
    path('categories/', views.Categories_view.as_view(), name='categories'),
    path('detailedinfo/', detailed_info.as_view(), name='detailedinfo'),
    path('binnacle/', binnacle.as_view(), name='binnacle'),
    path('ehome/', views.Home_view_employee.as_view(), name='employee_home'),
    path('gallery/', Gallery.as_view(), name ='gallery'),
    path('project/', Project_view.as_view(), name ='project'),
    path('convocatory/', Convocatory.as_view(), name='convocatory'),
    path('inscription/', Inscription.as_view(), name='inscription'),
    path('ehome/categories/',views.Employee_categories.as_view(),name='ecategories'),
    path('ehome/projects/',views.Employee_projects.as_view(),name='eprojects'),
    path('ehome/convocatories/',views.Employee_convocatories.as_view(),name='econvocatories'),
    path('ehome/clients/',views.Employee_clients.as_view(),name='eclients'),
    path('ehome/tools/',views.Employee_tools.as_view(),name='etools'),
]

urlpatterns += staticfiles_urlpatterns()