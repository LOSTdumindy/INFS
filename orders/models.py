from django.db import models
from core.models import Table
from menu.models import MenuItem

ORDER_STATUS = [
    ('ordered', 'Ordered'),
    ('preparing', 'Preparing'),
    ('ready', 'Ready'),
    ('complete', 'Complete'),
]

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='ordered')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()