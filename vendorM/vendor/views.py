from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import APIView

from .models import *
from .serializers import *

# Create your views here.

# FOR VENDOR.....................................
class VendorProfileManagementView(generics.CreateAPIView, generics.ListAPIView):
    queryset = VendorProfileManagement.objects.all()
    serializer_class = VendorProfileManagementSerializer


class VendorProfileManagementView2(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = VendorProfileManagement.objects.all()
    serializer_class = VendorProfileManagementSerializer
    lookup_field = 'vendor_code'

# For PURCHASE.....................................

class PurchaseOrderView(generics.CreateAPIView, generics.ListAPIView):
    queryset = PurchaseOrderModel()
    serializer_class = PurchaseOrderModelSerializer

class PurchaseOrderView2(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = PurchaseOrderModel()
    serializer_class = PurchaseOrderModelSerializer
    lookup_field = 'vendor_code'

# For VENDOR PERFORMANCE..........................

class HistoricalPerformanceView(generics.ListAPIView):
    queryset = HistoricalPerformanceModel()
    serializer_class = HistoricalPerformanceModelSerializer