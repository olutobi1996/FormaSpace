from django.urls import path
from . import views

app_name = 'enquiries'

urlpatterns = [
    path('', views.enquiry_create, name='enquiry_create'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
