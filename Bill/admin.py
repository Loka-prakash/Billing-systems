from django.contrib import admin
from .models import Bill, BillItem


class BillItemInline(admin.TabularInline):
    model = BillItem
    extra = 0


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'total_amount',
        'amount_paid',
        'created_at'
    )

    list_filter = ('created_at',)
    search_fields = ('email',)
    inlines = [BillItemInline]


@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'bill',
        'product_id',
        'price',
        'quantity',
        'subtotal'
    )
    search_fields = ('product_id',)

 
