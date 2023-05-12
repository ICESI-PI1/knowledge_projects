from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views
from core.views import detailed_info
from core.views import binnacle
from core.views import Project_view
from core.views import Gallery
from core.views import Donation_methods
from core.views import Successful_donation
app_name = 'core'
base_url_employee = 'ehome/'

urlpatterns = [
    path('', views.Home_view.as_view(), name='home'),
    path('home/', views.Home_view.as_view(), name='home'),
    path('categories/', views.Categories_view.as_view(), name='categories'),
    path('detailedinfo/', detailed_info.as_view(), name='detailedinfo'),
    path('binnacle/', binnacle.as_view(), name='binnacle'),
    path(base_url_employee, views.Home_view_employee.as_view(), name='employee_home'),
    path('gallery/', Gallery.as_view(), name ='gallery'),
    path('project/', Project_view.as_view(), name ='project'),
    path('donation_methods/', Donation_methods.as_view(), name='donation_methods'),
    path('successful_donation/', Successful_donation.as_view(), name='successful_donation'),
    path('ehome/categories/',views.Employee_categories.as_view(),name='ecategories'),
    path('ehome/projects/',views.Employee_projects.as_view(),name='eprojects'),
    path(base_url_employee+'categories/',views.Employee_categories.as_view(),name='ecategories'),
    path(base_url_employee+'convocatories/',views.Employee_convocatories.as_view(),name='econvocatories'),
    path(base_url_employee+'clients/',views.Employee_clients.as_view(),name='eclients'),
    path(base_url_employee+'tools/',views.Employee_tools.as_view(),name='etools'),
    path(base_url_employee+'categories/edit/<category_id>',views.Edit_category.as_view(),name='edit_category_ehome'),
    path(base_url_employee+'categories/delete/<category_id>',views.Delete_category.deleteCategory,name='delete_category_ehome'),
    path(base_url_employee+'categories/save',views.Save_Category.as_view(),name='save_category_ehome'),
    path(base_url_employee+'states/',views.Employee_states.as_view(),name='estates'),
    path(base_url_employee+'states/edit/<state_id>',views.Edit_state.as_view(),name='edit_state_ehome'),
    path(base_url_employee+'states/delete/<state_id>',views.Delete_state.delete_state,name='delete_state_ehome'),
    path(base_url_employee+'states/save',views.Save_state.as_view(),name='save_state_ehome'),
    
]

urlpatterns += staticfiles_urlpatterns()