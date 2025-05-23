# Generated by Django 5.1.7 on 2025-05-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkouts', '0002_orders_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_method',
            field=models.CharField(choices=[('cod', 'Cash on Delivery'), ('online', 'Online')], default='cod', max_length=10),
        ),
    ]
