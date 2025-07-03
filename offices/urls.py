from django.urls import path
from . import views


app_name = 'offices'

# offices/urls.py
urlpatterns = [
    path('co-working/', views.co_working, name='co_working'),
    path('private-office/', views.private_office, name='private_office'),
    path('virtual-office/', views.virtual_office, name='virtual_office'),
]



