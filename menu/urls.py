from django.urls import path
from .views import menu_view

app_name = 'menu'  

urlpatterns = [
    path('', menu_view, name='menu'), 
]
