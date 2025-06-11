from django.urls import path
from . import views

app_name = 'core'  # <-- this line is important if you're using namespaced URLs

urlpatterns = [
    path('', views.home, name='home'),
]
