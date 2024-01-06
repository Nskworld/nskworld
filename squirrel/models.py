from django.db import models
from django.utils import timezone

class Nutrition(models.Model):
    food_name = models.CharField(max_length=255, null=False)
    nutrient_name = models.CharField(max_length=255, null=False)
    amount = models.IntegerField(default=0, null=False)
    consumption_date = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return f"{self.food_name} ({self.consumption_date.strftime('%Y-%m-%d')})"

    class Meta:
        verbose_name_plural = "Nutritions"
