# Generated by Django 5.1.1 on 2024-10-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_alter_invoice_invoice_no_alter_invoice_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.IntegerField(),
        ),
    ]
