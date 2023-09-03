from django.urls import path
from .views import record

urlpatterns = [
    # Recordを管理するAPI
    path('record_list', record.record_list, name='record_list'),
    path('<int:pk>/', record.record_detail, name='record_detail'),
    path('new', record.record_new, name='record_new'),
    path('<int:pk>/edit/', record.record_edit, name='record_edit'),
    path('<int:pk>/delete/', record.record_delete, name='record_delete'),
    # Performanceを管理するAPI
    
]
