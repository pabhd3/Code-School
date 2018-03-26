# Python
# Django
# Try Django
# Getting Started (Level 1)
# Challenge 03 - Refactor the existing URL Dispatchers

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home), # added url object
]