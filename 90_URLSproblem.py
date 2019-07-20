#Day_90: This is the URLS.py file that seems to be tripping up on the runserver command (obviously not working at all)

from django.conf.urls import url
from . import views



app_name='accounts'

urlpatterns = [
    path('accounts/signup/', views.signup),

]
