from django.contrib import admin
from .models import Nutrition

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'consumption_date')
