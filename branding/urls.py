from django.urls import path
from . import views

app_name = 'branding'

urlpatterns = [
    path('', views.proposals_list, name='proposals_list'),
]
