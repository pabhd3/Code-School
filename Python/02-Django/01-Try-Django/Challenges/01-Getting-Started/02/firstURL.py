# Python
# Django
# Try Django
# Getting Started (Level 1)
# Challenge 01 - Create a simple view

from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # TODO: Create a url() object in the urlpatterns array.
    # TODO: Pass in the URL you’re matching, “home/” as a parameter to the url() object.
    # TODO: Pass in the corresponding views.home view as a parameter to the url() object.
]