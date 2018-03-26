# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 12 - Refactor view to use model

from django.shortcuts import render
from .models import Location # imported Locations

def home(request):
    locations = Location.objects.all() # made a list using QuerySet
    return render(request, 'home.html', {'locations': locations})