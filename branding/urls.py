from django.urls import path
from . import views

app_name = 'branding'

urlpatterns = [
    path('about/', views.about, name='about'),
]

