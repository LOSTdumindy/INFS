from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from menu.models import MenuItem
from .models import Cart, CartItem

@login_required
def add_to_cart(request, item_id):
    try:
        item = MenuItem.objects.get(id=item_id)
    except MenuItem.DoesNotExist:
        return redirect('menu:menu')
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=item)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    
    return redirect('menu:menu')

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return redirect('menu:menu')
    
    items = cart.items.all()
    total = sum(item.total_price() for item in items)
    
    return render(request, 'cart.html', {'items': items, 'cart_total': total})

@login_required
def remove_from_cart(request, item_id):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, menu_item_id=item_id)
        cart_item.delete()
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        pass
    
    return redirect('cart:view_cart')

@login_required
def update_quantity(request, item_id):
    quantity = int(request.POST.get("quantity"))
    cart = Cart.objects.get(user=request.user, is_active=True)
    cart_item = CartItem.objects.get(cart=cart, menu_item_id=item_id)
    cart_item.quantity = quantity
    cart_item.save()
    
    return redirect('cart:view_cart')
