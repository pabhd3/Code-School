from django.shortcuts import render
from .models import Location # imported Locations

def home(request):
    locations = Location.objects.all()
    return render(request, 'home.html', {'locations': locations})