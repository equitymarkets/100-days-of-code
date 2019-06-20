from django.db import models

# Create your models here.
class Goal(models.Model):
    """I plan to define project goals here by time"""
    text = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the string to page"""
        return self.text

class Description(models.Model):
    """Description of goal and projected date of completion"""
    topic = models.ForeignKey(Goal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Returns the description of the goal"""
        return self.text[:100] + "..."
