"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

# Custom Error Handlers
handler404 = 'myapp.views.custom_404'
handler500 = 'myapp.views.custom_500'
