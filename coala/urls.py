from django.urls import path
from .views import record, performance, challenge

urlpatterns = [
    # Recordを管理するAPI
    path('record/list', record.record_list, name='record_list'),
    path('record/<int:pk>/', record.record_detail, name='record_detail'),
    path('record/new', record.record_new, name='record_new'),
    path('record/<int:pk>/edit/', record.record_edit, name='record_edit'),
    path('record/<int:pk>/delete/', record.record_delete, name='record_delete'),
    # Performanceを管理するAPI
    path('performance/list', performance.performance_list, name='performance_list'),
    path('performance/new', performance.performance_new, name='performance_new'),
    path('performance/<int:pk>/edit/', performance.performance_edit, name='performance_edit'),
    path('performance/<int:pk>/delete/', performance.performance_delete, name='performance_delete'),
    # Challengeを管理するAPI
    path('challenge/list', challenge.challenge_list, name='challenge_list'),
    path('challenge/<int:pk>/', challenge.challenge_detail, name='challenge_detail'),
    path('challenge/new', challenge.challenge_new, name='challenge_new'),
    path('challenge/<int:pk>/edit/', challenge.challenge_edit, name='challenge_edit'),
    path('challenge/evaluation/<int:pk>/edit/', challenge.evaluation_edit, name='evaluation_edit'),
    path('challenge/<int:pk>/delete/', challenge.challenge_delete, name='challenge_delete')
]
