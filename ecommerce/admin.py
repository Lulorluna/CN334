from django.contrib import admin

# Register your models here.
from .models import Customer
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel')
    list_filter = ('province',)
    ordering = ('id',)