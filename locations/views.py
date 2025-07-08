from django.shortcuts import render
from .models import Location

def location(request):
    locations = Location.objects.filter(is_active=True)
    return render(request, 'locations/location.html', {'locations': locations})

