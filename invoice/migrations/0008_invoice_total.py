# Generated by Django 5.1.1 on 2024-10-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_remove_invoice_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
