from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel')
    list_filter = ('province',)
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    ordering = ('id',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_owner', 'method', 'card_no', 'expired', 'holder_name')
    search_fields = ('payment_owner__username', 'holder_name', 'card_no')
    list_filter = ('method',)

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'method', 'fee')
    search_fields = ('method',)
    ordering = ('id',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status', 'shipping', 'payment', 'create_at', 'update_at')
    search_fields = ('customer__username', 'status')
    list_filter = ('status',)
    ordering = ('id',)

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity', 'total_price')
    search_fields = ('product__name', 'order__id')
    ordering = ('id',)