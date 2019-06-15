#Day 58: The following is the addition to the models.py file in the forest app

class Entry(models.Model):
    topic = models.ForeignKey(Objective, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return self.text[:50] + "..."
