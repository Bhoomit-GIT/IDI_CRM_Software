# Generated by Django 5.1.1 on 2024-10-27 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0002_delete_connection_bank_details_connection_c_gstin_and_more'),
        ('invoice', '0009_alter_invoice_invoice_no_alter_invoiceitem_product_and_more'),
        ('products', '0004_remove_product_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='connection',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='connections.connection'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
