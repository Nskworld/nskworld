from django.db import models

class Emotion(models.Model):
    name = models.CharField(max_length=10)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name