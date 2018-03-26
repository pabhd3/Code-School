# Python
# Django
# Try Django
# Getting Started (Level 1)
# Challenge 03 - Refactor the existing URL Dispatchers

from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')), # empty path, and included app urls
]