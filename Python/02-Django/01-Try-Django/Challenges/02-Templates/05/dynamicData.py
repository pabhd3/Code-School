# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 05 - Pass dynamic data to a template

from django.shortcuts import render

def home(request):
    location_name = "Flavortown"
    flavors = 'Sweet, Sour, Spicy'
    # TODO: Create a dictionary object that with key-value pairs of 
    #       location_name and flavors
    # TODO: Pass the dictionary object as a parameter in the return render
    return render(request, 'home.html')