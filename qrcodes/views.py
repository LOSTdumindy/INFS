import qrcode
from io import BytesIO
import base64
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from core.models import Table
import requests


def generate_qr(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    url = f"http://127.0.0.1:8000/order/place/?table={table.code}"

    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'show_qr.html', {
        'table': table,
        'qr_base64': img_base64,
        'url': url
    })



def qr_scanner(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]

        try:
            response = requests.post(
                "https://api.qrserver.com/v1/read-qr-code/",
                files={"file": image_file}
            )

            data = response.json()
            qr_data = data[0]['symbol'][0]['data'] if data else None

            if qr_data:
                if qr_data.startswith("/"):
                    full_url = request.build_absolute_uri(qr_data)
                    return redirect(full_url)
                elif qr_data.startswith("http"):
                    return redirect(qr_data)
                else:
                    messages.error(request, "Invalid QR code format.")
            else:
                messages.error(request, "QR code could not be read.")

        except Exception as e:
            messages.error(request, f"Error scanning image: {str(e)}")

    return render(request, 'qr_scanner.html')