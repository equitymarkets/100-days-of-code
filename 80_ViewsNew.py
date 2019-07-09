#Day 80: There is still an error somewhere tracing back to this page re my project blog that I am trying to create. 
#Two base files in same app?

from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Topic
from django.http import HttpResponseRedirect
from django.shortcuts import render

#from .forms import NameForm


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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forest:index')
        else:
            form = UserCreationForm()
        return render(request, '/register.html',{'form': form })

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

def menu_8(request):
    context = {'menu_8': menu_8}
    return render(request, 'forest/menu_8.html')

def myitems(request):
    context = {'myitems': myitems}
    return render(request, 'forest/myitems.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'forest/topics.html', context)
    
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'forest/topic.html', context)
