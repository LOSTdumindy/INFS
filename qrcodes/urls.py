from django.urls import path
from .views import generate_qr,qr_scanner

urlpatterns = [
     path('generate/<int:table_id>/', generate_qr, name='generate_qr'), 
    path('scanner/', qr_scanner, name='qr_scanner'),
]
