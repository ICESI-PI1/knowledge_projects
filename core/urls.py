from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views
from core.views import detailed_info
from core.views import binnacle
from core.views import Project
from core.views import Gallery
<<<<<<< refs/remotes/origin/Project_views
from core.views import Convocatory
from core.views import Inscription
=======
from core.views import Donation_methods
from core.views import Successful_donation
>>>>>>> local
app_name = 'core'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('home/', views.Home_view.as_view(), name='home'),
    path('categories/', views.Categories_view.as_view(), name='categories'),
    path('detailedinfo/', detailed_info.as_view(), name='detailedinfo'),
    path('binnacle/', binnacle.as_view(), name='binnacle'),
    path('gallery/', Gallery.as_view(), name ='gallery'),
<<<<<<< refs/remotes/origin/Project_views
    path('project/', Project.as_view(), name ='project'),
    path('convocatory/', Convocatory.as_view(), name='convocatory'),
    path('inscription/', Inscription.as_view(), name='inscription'),
=======
    path('project/', Project_view.as_view(), name ='project'),
    path('donation_methods/', Donation_methods.as_view(), name='donation_methods'),
    path('successful_donation/', Successful_donation.as_view(), name='successful_donation'),
    path('ehome/categories/',views.Employee_categories.as_view(),name='ecategories'),
    path('ehome/projects/',views.Employee_projects.as_view(),name='eprojects'),
    path('ehome/convocatories/',views.Employee_convocatories.as_view(),name='econvocatories'),
    path('ehome/clients/',views.Employee_clients.as_view(),name='eclients'),
    path('ehome/tools/',views.Employee_tools.as_view(),name='etools'),
>>>>>>> local
]

urlpatterns += staticfiles_urlpatterns()