from django.shortcuts import render, redirect
from .models import MenuItem

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})
