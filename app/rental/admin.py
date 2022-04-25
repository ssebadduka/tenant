from django.contrib import admin
from .models import Tenant,Room,Contract,Property,Payment


@admin.register(Payment)
# admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'contract','date_paid','monthly_rent_due','amount_paid','Balance','receipt_number','date_paid')

# Register your models here.
admin.site.register(Tenant)
admin.site.register(Room)
admin.site.register(Contract)
admin.site.register(Property)
admin.site.site_header = "BITIJUMA INVESTMENTS"
admin.site.site_title = "BITIJUMA INVESTMENTS"
admin.site.index_title = "BITIJUMA INVESTMENTS"

