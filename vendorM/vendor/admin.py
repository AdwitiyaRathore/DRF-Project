from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(VendorProfileManagement)
admin.site.register(PurchaseOrderModel)
admin.site.register(HistoricalPerformanceModel)