from django.shortcuts import render, get_object_or_404
from .models import Location

def private_office(request):
    return render(request, 'offices/private_office.html', {'video': True})  


def co_working(request):
    context = {
        'video': True,  # or False if you want to control this dynamically
    }
    return render(request, 'offices/co-working.html', context)
    

def virtual_office(request):
    return render(request, 'offices/virtual_office.html', {'video': True})


def meeting_rooms(request):
    return render(request, 'offices/meeting_rooms.html', {'video': True}) 