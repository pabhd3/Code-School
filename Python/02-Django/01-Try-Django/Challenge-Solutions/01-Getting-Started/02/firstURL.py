# Python
# Django
# Try Django
# Getting Started (Level 1)
# Challenge 02 - Create a simply URL pattern

from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home) # added view to urlpatterns
]