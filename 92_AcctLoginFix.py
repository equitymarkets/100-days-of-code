#Day 92: Be sure to import path any time you are calling the path to a URL

from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    #url(r'signup/$', views.signup_view, name="signup")
]
