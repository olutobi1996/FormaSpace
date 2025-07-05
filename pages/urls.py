from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('connectivity/', views.connectivity_view, name='connectivity'),
]
