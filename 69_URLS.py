#Day 69 - It seems the problem in the code (if it is indeed in this page, and I'm pretty sure this page is a big part of it) is 
#on Line 24. I am learning, but that is a little confusing for me right now. 

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
    path('blog/<int:description_id>/', views.blog, name='blog'),
    #Show all topics
    #path('topics/', views.topics, name='topics'),
    #Detail page for a single topic
    #path('topics/<int:topic_id>/', views.topic, name='topic'),
    
]

#urlpatterns += staticfiles_urlpatterns()
