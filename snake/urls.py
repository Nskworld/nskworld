from django.urls import path
from .views import emotion

urlpatterns = [
    path('', emotion.emotion_list, name='emotion_list'),
    path('new', emotion.emotion_new, name='emotion_new'),
    path('<int:pk>/delete/', emotion.emotion_delete, name='emotion_delete'),
]