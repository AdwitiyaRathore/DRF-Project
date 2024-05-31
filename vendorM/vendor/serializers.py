from rest_framework import serializers

from .models import *


class VendorProfileManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProfileManagement
        fields = '__all__'
    
    def validate(self, attr):
        contact = attr['contact_details']

        if len(contact) == 10:
            return attr
        else:
            raise serializers.ValidationError({'Error': 'Contact number should contain 10 digits. '})

class PurchaseOrderModelSerializer(serializers.ModelSerializer):
    vendor = VendorProfileManagementSerializer()

    class Meta: 
        model = PurchaseOrderModel
        fields = '__all__'

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        if validated_data.get('status') == 'completed':
            update_vendor_performance(instance.vendor)

        if 'acknowledgment_date' in validated_data:
            update_vendor_performance(instance.vendor)

        return instance

class HistoricalPerformanceModelSerializer(serializers.ModelSerializer):
    vendor = VendorProfileManagementSerializer()

    class Meta:
        model = HistoricalPerformanceModel
        fields = '__all__'

def update_vendor_performance(vendor):

    # On time Delivery Rate
    completed_pos = PurchaseOrderModel.objects.filter(vendor=vendor, status='completed')
    on_time_pos = completed_pos.filter(delivery_date_lte=models.F('delivery_date'))
    on_time_delivery_rate = on_time_pos.count()/ completed_pos.count() if completed_pos > 0 else 0

    # Quality Rating Average
    quality_ratings = completed_pos.filter(quality_rating__isnull = False).values_list('quality_ratings', flat=True)
    quality_ratings_avg = sum(quality_ratings)/ len(quality_ratings) if quality_ratings > 0 else 0


    # Average Response Time

    response_times = [
        (po.acknowledgement_date - po.issue_date).total_seconds() for po in PurchaseOrderModel.objects.filter(vendor=vendor, acknowledgement_date__isnull=False)

    ]
    average_response_time = sum(response_times)/len(response_times) if response_times else 0

    # Fulfilment Rate

    total_pos = PurchaseOrderModel.objects.filter(vendor=vendor).count()
    fulfilled_pos = completed_pos.count()
    fulfilled_rate = fulfilled_pos/ total_pos if total_pos > 0 else 0

    # Update or create the historical performance record

    HistoricalPerformanceModel.objects.update_or_create(
        vendor=vendor,
        defaults={
            'on_time_delivery_rate' : on_time_delivery_rate,
            'quality_rating_avg' : quality_ratings_avg,
            'average_response_time' : average_response_time,
            'fulfillment_rate' : fulfilled_rate
        }
    )