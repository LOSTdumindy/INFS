from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from menu.models import MenuItem
from core.models import Table
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.contrib import messages

def place_order(request):
    table_code = request.GET.get("table")

    table = None
    if table_code:
        table = get_object_or_404(Table, code=table_code)

    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Your order has been placed successfully!")
        return redirect('cart:view_cart')

    order = Order.objects.create(table=table)

    for item_id, qty in cart.items():
        item = get_object_or_404(MenuItem, id=item_id)
        OrderItem.objects.create(order=order, item=item, quantity=qty)

    request.session['cart'] = {}

    messages.success(request, "Your order has been placed successfully!")

    return redirect('cart:view_cart')



def update_status(request, order_id, new_status):
    order = get_object_or_404(Order, id=order_id)
    order.status = new_status
    order.save()
    return HttpResponseRedirect(reverse('dashboard'))



def dashboard_view(request):
    today = now().date()
    orders_today = Order.objects.filter(created_at__date=today)
    revenue = sum(sum(item.item.price * item.quantity for item in order.items.all()) for order in orders_today)
    avg_order = revenue / orders_today.count() if orders_today.exists() else 0

    popular = {}
    for item in OrderItem.objects.all():
        popular[item.item.name] = popular.get(item.item.name, 0) + item.quantity
    popular_items = sorted([
        {"name": name, "count": count} for name, count in popular.items()
    ], key=lambda x: x['count'], reverse=True)[:5]

    active_orders = Order.objects.exclude(status='complete')
    return render(request, 'dashboard.html', {
        'orders_today': orders_today.count(),
        'revenue': revenue,
        'avg_order': avg_order,
        'popular_items': popular_items,
        'active_orders': active_orders
    })