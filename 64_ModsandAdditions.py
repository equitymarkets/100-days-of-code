#from urls.py:

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forest.urls')),]


#from new urls.py app file:

from django.urls import path

from . import views

app_name = 'forest'
urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    path('', views.menu_1, name='menu_1'),
    

from views.py: 

from django.shortcuts import render

def index(request):
    """Home Page"""
    return render(request, 'forest/index.html')

def menu_1(request):
    return render(request, 'forest/menu_1.html')
