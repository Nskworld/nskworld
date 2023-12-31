from django.db import models

class Log(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
