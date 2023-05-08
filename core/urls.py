from django.urls import include, path

from core import views
from core.views import detailed_info
from core.views import binnacle
app_name = 'core'

urlpatterns = [
    path('home/', views.home, name ='home'),
     path('detailedinfo/', detailed_info.as_view(), name='detailedinfo'),
    path('binnacle/', binnacle.as_view(), name='binnacle'),
]