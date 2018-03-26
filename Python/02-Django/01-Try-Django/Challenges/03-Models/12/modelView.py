# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 12 - Refactor view to use model

from django.shortcuts import render
# TODO: Import the Location model from .models
def home(request):
    # TODO: Create a list object called locations, and set it equal to all() 
    #       of the objects in the Location model using a QuerySet
    return render(request, 'home.html', {'locations': locations})