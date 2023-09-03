from django.db import models

class Record(models.Model):
    time_going_bed = models.IntegerField()
    time_falling_asleep = models.IntegerField()
    time_getting_up = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

