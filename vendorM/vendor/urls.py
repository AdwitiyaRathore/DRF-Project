from django.urls import path

from .views import *

urlpatterns = [
    # Vendor Profile Management URLs
    path('vendor/', VendorProfileManagementView.as_view(), name='vendor-list-create'),
    path('vendor/<str:vendor_code>/', VendorProfileManagementView2.as_view(), name='vendor-detail-update-delete'),
    
    # Purchase Order URLs
    path('purchase/', PurchaseOrderView.as_view(), name='purchase-list-create'),
    path('purchase/<int:id>/', PurchaseOrderView2.as_view(), name='purchase-detail-update-delete'),
    
    # Historical Performance URLs
    path('performance/', HistoricalPerformanceView.as_view(), name='performance-list'),
]