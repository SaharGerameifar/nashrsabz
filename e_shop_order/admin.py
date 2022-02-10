from django.contrib import admin

from .models import (Order, OrderDetail)



class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner_username', 'jpayment_date', 'is_paid', 'ref_id']
    ordering = ['-payment_date']
    list_filter = (['is_paid'])
    search_fields = ['ref_id']


    def owner_username(self, obj):
        if obj.owner.get_full_name():
            return obj.owner.get_full_name()
        return obj.owner.username
    owner_username.short_description = 'مالک سبد خرید'

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
