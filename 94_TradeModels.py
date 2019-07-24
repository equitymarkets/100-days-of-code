from django.db import models

class Offer(models.Model):
    """Trade Offers"""
    item = models.TextField(max_length=60)
    amount = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """Return the string to page"""
        return self.item

class Want(models.Model):
    """Wish List"""
    item = models.TextField(max_length=60)
    amount = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """Return the string to page"""
        return self.item
