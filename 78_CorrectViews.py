from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.http import HttpResponseRedirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forest:index')
    else: 
        form = UserCreationForm()
    return render(request,"accounts/signup.html", {'form': form})
