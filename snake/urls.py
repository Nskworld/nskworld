from django.urls import path
from .views import emotion

urlpatterns = [
    path('', emotion.emotion_list, name='emotion_list'),
    path('new', emotion.log_new, name='emotion_new'),
    path('<int:pk>/delete/', emotion.log_delete, name='emotion_delete'),
]