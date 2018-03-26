# Python
# Django
# Try Django
# Templates (Level 3)
# Challenge 13 - Register an admin

from django.contrib import admin
from .models import Location # imported Location model

# Register your models here.
admin.site.register(Location) # registered Location model