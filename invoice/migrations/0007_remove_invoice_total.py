# Generated by Django 5.1.1 on 2024-10-16 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_alter_invoice_invoice_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='total',
        ),
    ]
