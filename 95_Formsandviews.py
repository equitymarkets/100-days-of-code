#Day 95: Learned about forms.py file and worked in html to create Django functionality with them-they aren't working correctly yet 

#forms.py:


from django import forms

class OfferForm(forms.Form):
    post = forms.CharField()
 
 #views.py:
 
 from django.shortcuts import render
from django.views.generic import TemplateView
from trades.forms import OfferForm



class offer_view(TemplateView):
    template_name = 'forest/index.html'
    def get(self, request):
        form = OfferForm()
        return render(request, self.template_name, {'form': form})

