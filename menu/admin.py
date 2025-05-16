from django.contrib import admin
from .models import Category, MenuItem
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_count')
    search_fields = ('name',)
    ordering = ('name',)

    def item_count(self, obj):
        count = obj.items.count()
        return format_html(
            '<span style="color:#10B981;font-weight:bold;">{} item{}</span>',
            count, 's' if count != 1 else ''
        )
    item_count.short_description = 'Total Items'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('styled_name', 'category', 'price_badge', 'short_description')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('category', 'name')
    list_per_page = 20

    def styled_name(self, obj):
        return format_html(
            '<span style="font-weight:600;color:#374151;">{}</span>',
            obj.name
        )
    styled_name.short_description = 'Menu Item'

    def price_badge(self, obj):
        return format_html(
            '<div style="background:#F59E0B;padding:4px 10px;border-radius:12px;color:white;font-weight:bold;">${}</div>',
            obj.price
        )
    price_badge.short_description = 'Price'

    def short_description(self, obj):
        if not obj.description:
            return format_html('<span style="color:gray;">No description</span>')
        return format_html('<span>{}</span>', obj.description[:40] + '...')
    short_description.short_description = 'Description'
