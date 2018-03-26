# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 06 - Create a simple class

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class Location:
    def __init__(self, name, flavors, num_franchises, image):
        self.name = name
        self.flavors = flavors # added flavor attribute
        self.num_franchises = num_franchises # added num_franchises attribute
        self.image = image # added image attribute
