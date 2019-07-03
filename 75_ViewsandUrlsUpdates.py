#Day 75: A few .py updates here
#Urls.py
"""Defines URL patterns for forest."""
from django.urls import path
from . import views

app_name = 'forest'

urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    #Sub pages
    path('menu_1/', views.menu_1, name='menu_1'),
    path('menu_2/', views.menu_2, name='menu_2'),
    path('menu_3/', views.menu_3, name='menu_3'),
    path('menu_4/', views.menu_4, name='menu_4'),
    path('menu_5/', views.menu_5, name='menu_5'),
    path('menu_6/', views.menu_6, name='menu_6'),
    path('menu_7/', views.menu_7, name='menu_7'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('blog/<int:description_id>/', views.blog, name='blog'),
    #Show all topics
    #path('topics/', views.topics, name='topics'),
    #Detail page for a single topic
    #path('topics/<int:topic_id>/', views.topic, name='topic'),
    
]

#urlpatterns += staticfiles_urlpatterns()

#Views.py

from django.shortcuts import render
from .models import Goal

def index(request):
    """Home Page"""
    return render(request, 'forest/index.html')

def blog(request):
    """Admin Blog Page: Goals and Timeline"""
    context = {'blog': blog}
    return render(request, 'forest/blog.html')

def login(request):
    context = {'login': login}
    return render(request, 'forest/login.html')

def register(request):
    context = {'register': register}
    return render(request, 'forest/register.html')

def menu_1(request):
    context = {'menu_1': menu_1}
    return render(request, 'forest/menu_1.html')

def menu_2(request):
    context = {'menu_2': menu_2}
    return render(request, 'forest/menu_2.html')
    
def menu_3(request):
    context = {'menu_3': menu_3}
    return render(request, 'forest/menu_3.html')

def menu_4(request):
    context = {'menu_4': menu_4}
    return render(request, 'forest/menu_4.html')

def menu_5(request):
    context = {'menu_5': menu_5}
    return render(request, 'forest/menu_5.html')

def menu_6(request):
    context = {'menu_6': menu_6}
    return render(request, 'forest/menu_6.html')

def menu_7(request):
    context = {'menu_7': menu_7}
    return render(request, 'forest/menu_7.html')

def myitems(request):
    context = {'myitems': myitems}
    return render(request, 'forest/myitems.html')



def goals(request):
    goals = Goal.objects.order_by('date_added')
    context = {'goals': goals}
    return render(request, 'forest/blog.html', context)
    
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    goal = Goal.objects.get(id=topic_id)
    entries = goal.entry_set.order_by('-date_added')
    context = {'goal': goal, 'entries': entries}
    return render(request, 'forest/blog.html', context)
