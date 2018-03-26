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
    url(r'^home/', views.home) # added view to urlpatterns
]