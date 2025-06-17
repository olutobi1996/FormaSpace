from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/',       views.about_view,       name='about'),
    path('connections/', views.connections_view, name='connections'),
]
