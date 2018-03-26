# Python
# Django
# Try Django
# Getting Started (Level 1)
# Challenge 01 - Create a simple view

from django.http import HttpResponse

def home(request): # Created home() function with "request" parameter
    return HttpResponse("Welcome Home Eaters!") # returned HttpResponse