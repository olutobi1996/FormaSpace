from django.shortcuts import render
from .models import Location

def location_list(request):
    locations = Location.objects.filter(is_active=True)
    return render(request, 'locations/location_list.html', {'locations': locations})

