# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 04 - Update an existing template

from django.http import HttpResponse
from django.shortcuts import render # imported render

def home(request):
    return render(request, 'home.html') # returned render object