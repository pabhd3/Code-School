# Python
# Django
# Try Django
# Templates (Level 2)
# Challenge 07 - Create a list of class objects

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class Location:
    def __init__(self, name, flavors, num_franchises, image):
        self.name = name
        self.flavors = flavors
        self.num_franchises = num_franchises
        self.image = image

locations = [
    Location("Banana-Rama, MI", 'Sweet', 0,
             "https://www.omnihotels.com/-/media/images/hotels/bospar/restaurants/bospar-omni-parker-house-parkers-restaurant-1170.jpg"),
    Location("The Little Man, MO", 'Sour', 2,
             "https://file.videopolis.com/D/9dc9f4ba-0b2d-4cbb-979f-fee7be8a4198/8485.11521.brussels.the-hotel-brussels.amenity.restaurant-AD3WAP2L-13000-853x480.jpeg"),
    Location("The Hill Top, CT", "Savory", 1,
             "http://www.gffoodservice.org/wp-content/uploads/2015/03/restaurant-e1456862749354.jpg")
]