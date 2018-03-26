# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 11 - Create a simple model

from django.db import models

class Location(models.Model):
    # TODO: Add the following fields to the model, with the correct Django 
    #       field types:
    # 	        “name” - a string, “flavors” - a string, 
    #           “num_franchises” - an integer, “image” - a string
    # TODO: Set the CharField() types to have a max_length of 75.
    # TODO: Add a __str__ method that will return the self.name value.