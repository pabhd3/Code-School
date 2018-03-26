from django.db import models

# Create your models here.
class Location(models.Model):
    # added fields and parameters
    name = models.CharField(max_length=75)
    flavors = models.CharField(max_length=75)
    num_franchises = models.IntegerField()
    image = models.CharField(max_length=75)
    # added __str__ method
    def __str__(self):
        return self.name