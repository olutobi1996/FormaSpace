from django.shortcuts import render
from core.models import MyVideo

def home(request):
    video = MyVideo.objects.first()  
    return render(request, 'core/home.html', {'video': video})
