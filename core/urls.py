from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views
from core.views import detailed_info
from core.views import binnacle
from core.views import Project
from core.views import Gallery
from core.views import Convocatory
from core.views import Inscription
from core.views import Donation_methods
from core.views import Successful_donation
app_name = 'core'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('home/', views.Home_view.as_view(), name='home'),
    path('categories/', views.Categories_view.as_view(), name='categories'),
    path('detailedinfo/', detailed_info.as_view(), name='detailedinfo'),
    path('binnacle/', binnacle.as_view(), name='binnacle'),
    path('gallery/', Gallery.as_view(), name ='gallery'),
    path('project/', Project.as_view(), name ='project'),
    path('convocatory/', Convocatory.as_view(), name='convocatory'),
    path('inscription/', Inscription.as_view(), name='inscription'),
    path('donation_methods/', Donation_methods.as_view(), name='donation_methods'),
    path('successful_donation/', Successful_donation.as_view(), name='successful_donation'),
]

urlpatterns += staticfiles_urlpatterns()