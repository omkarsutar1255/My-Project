# Generated by Django 4.2.7 on 2023-11-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0005_alter_purchaseorder_quality_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='on_time_delivery',
            field=models.BooleanField(default=False),
        ),
    ]
