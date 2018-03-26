# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 04 - Update an existing template

from django.http import HttpResponse
# TODO: Import render from django.shortcuts

def home(request):
    # TODO: Update the home() function to return a render object that takes 
    #       in a request object, and the home.html template
    return HttpResponse('Welcome Home Eaters!')
