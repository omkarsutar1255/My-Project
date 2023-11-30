# Generated by Django 4.2.7 on 2023-11-27 04:29

import Vendor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_alter_vendor_average_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20, null=True, validators=[Vendor.models.validate_status]),
        ),
    ]
