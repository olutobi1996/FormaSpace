from django.urls import path
from . import views

app_name = 'offices'

urlpatterns = [
    path('', views.location_list, name='location_list'),
    path('<int:pk>/', views.location_detail, name='location_detail'),
]
