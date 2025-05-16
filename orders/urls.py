from django.urls import path
from .views import place_order, update_status, dashboard_view

app_name = 'orders'

urlpatterns = [
    path('place/', place_order, name='place_order'),
    path('status/<int:order_id>/<str:new_status>/', update_status, name='update_status'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
