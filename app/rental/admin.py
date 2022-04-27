from django.contrib import admin
from .models import Tenant,Room,Contract,Property,Payment


@admin.register(Payment)
# admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('tenant','date_paid','amount_paid','paid_from','paid_to','Balance','receipt_number')

# Register your models here.
admin.site.register(Tenant)
admin.site.register(Room)
admin.site.register(Contract)
admin.site.register(Property)
admin.site.site_header = "BITIJUMA INVESTMENTS"
admin.site.site_title = "BITIJUMA INVESTMENTS"
admin.site.index_title = "BITIJUMA INVESTMENTS"

