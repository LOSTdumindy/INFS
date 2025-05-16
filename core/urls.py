from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('table/<str:code>/', views.table_menu_view, name='table_menu'),
    path('generate-qr/<int:table_id>/', views.generate_qr, name='generate_qr'),
]
