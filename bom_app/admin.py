from django.contrib import admin
from .models import Product, BOMItem

class BOMItemInline(admin.TabularInline):
    model = BOMItem
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    inlines = [BOMItemInline]

class BOMItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'item_name', 'item_type', 'custom_item_type',
        'quantity', 'unit'
    )
    list_filter = ('item_type', 'unit')
    search_fields = ('item_name', 'custom_item_type')


admin.site.register(Product, ProductAdmin)
admin.site.register(BOMItem, BOMItemAdmin)
