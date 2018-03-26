# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 05 - Pass dynamic data to a template

from django.shortcuts import render

def home(request):
    location_name = "Flavortown"
    flavors = 'Sweet, Sour, Spicy'
    # Created dictionary object
    context = {"location_name": location_name,
               "flavors": flavors}
    return render(request, 'home.html', context) # passed it to render object