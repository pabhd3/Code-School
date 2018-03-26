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
    # TODO: Edit the second url() object to include(‘main.urls’)
    # TODO: Change the regex parameter to match a blank path
    url(r'^home/', views.home),
]