import qrcode
from django.http import JsonResponse
from .models import Table
from django.shortcuts import get_object_or_404
from io import BytesIO
import base64
from django.shortcuts import render, get_object_or_404
from .models import Table
from menu.models import MenuItem
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home.html')


def generate_qr(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    url = f"http://127.0.0.1:8000/table/{table.code}/"
    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode()

    return JsonResponse({
        "table_id": table.id,
        "code": table.code,
        "qr_base64": img_base64,
        "url": url
    })
    

def table_menu_view(request, code):
    table = get_object_or_404(Table, code=code)
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items, 'table': table})
