from django.urls import path
from .views import upload_csv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
