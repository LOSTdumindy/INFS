from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, update_quantity

app_name = 'cart'

urlpatterns = [
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('view/', view_cart, name='view_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', update_quantity, name='update_quantity'),
]
