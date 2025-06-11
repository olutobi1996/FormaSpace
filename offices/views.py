from django.shortcuts import render, get_object_or_404
from .models import Location

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'offices/location_list.html', {'locations': locations})

def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'offices/location_detail.html', {'location': location})

