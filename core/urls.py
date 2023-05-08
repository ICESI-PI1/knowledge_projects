from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views
from core.views import detailed_info
from core.views import binnacle
app_name = 'core'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('home/', views.Home_view.as_view(), name='home'),
    path('categories/', views.Categories_view.as_view(), name='categories'),
    path('detailedinfo/', detailed_info.as_view(), name='detailedinfo'),
    path('binnacle/', binnacle.as_view(), name='binnacle'),
]

urlpatterns += staticfiles_urlpatterns()