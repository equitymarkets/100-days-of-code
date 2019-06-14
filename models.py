from django.db import models



# Create your models here.
class Objective(models.Model):
    OFFER = 'OF'
    SEARCH = 'SC'
    offer_or_searchfor = [(OFFER, 'offer'), (SEARCH, 'search')]
    need = models.CharField(max_length=2, choices=offer_or_searchfor, 
        default=OFFER)
    date = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.text
