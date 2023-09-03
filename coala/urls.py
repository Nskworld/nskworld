from django.urls import path
from .views import record, performance

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
]
