#New urls.py:

"""Defines URL patterns for forest."""
from django.urls import path

from . import views

app_name = 'forest'

urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    #Sub pages
    path('menu_1/', views.menu_1, name='menu_1'),
    
#New views.py:

from django.shortcuts import render

def index(request):
    """Home Page"""
    return render(request, 'forest/index.html')

def menu_1(request):
     
    context = {'menu_1': menu_1}
    return render(request, 'forest/menu_1.html')
