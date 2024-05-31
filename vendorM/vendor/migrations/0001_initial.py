# Generated by Django 5.0.6 on 2024-05-29 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VendorProfileManagement",
            fields=[
                ("name", models.CharField(max_length=20)),
                ("contact_details", models.TextField(max_length=10)),
                ("address", models.TextField()),
                (
                    "vendor_code",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("on_time_delivery_rate", models.FloatField()),
                ("quality_rating_avg", models.FloatField()),
                ("average_response_time", models.FloatField()),
                ("fulfillment_rate", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrderModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("po_number", models.CharField(max_length=10, unique=True)),
                ("order_date", models.DateTimeField(auto_now=True)),
                ("delivery_date", models.DateTimeField()),
                ("items", models.JSONField()),
                ("quantity", models.IntegerField()),
                ("status", models.CharField(max_length=20)),
                ("quality_rating", models.FloatField()),
                ("issue_date", models.DateTimeField()),
                ("acknowledgment_date", models.DateTimeField()),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vendor.vendorprofilemanagement",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalPerformanceModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("on_time_delivery_rate", models.FloatField()),
                ("quality_rating_avg", models.FloatField()),
                ("average_response_time", models.FloatField()),
                ("fulfillment_rate", models.FloatField()),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vendor.vendorprofilemanagement",
                    ),
                ),
            ],
        ),
    ]
