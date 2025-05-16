# core/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from io import BytesIO
import qrcode
import base64
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('styled_number', 'code', 'qr_code_preview')
    search_fields = ('number', 'code')
    ordering = ('number',)
    list_per_page = 20

    def styled_number(self, obj):
        return format_html(
            '<div style="background:#4B5563;color:white;padding:6px 12px;border-radius:8px;display:inline-block;font-weight:bold;">Table {}</div>',
            obj.number
        )
    styled_number.short_description = 'Table Number'

    def qr_code_preview(self, obj):
        """Generate and return a preview of the QR code for the table."""
        url = reverse('generate_qr', args=[obj.id])  # Generate URL for QR code page
        qr_code_img = self.generate_qr_code(url)
        return format_html(
            '<div style="padding:5px;border:1px dashed #ccc;border-radius:8px;">'
            '🧾 Code: <b>{}</b><br>'
            '<img src="data:image/png;base64,{}" alt="QR Code" style="width:100px;height:100px;border-radius:8px;"/>'
            '</div>', obj.code, qr_code_img
        )
    qr_code_preview.short_description = 'QR Code Preview'

    def generate_qr_code(self, url):
        """Generate a QR code image and return it as a base64 string."""
        img = qrcode.make(url)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        return img_base64
