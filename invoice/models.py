from django.db import models
from products.models import Product
from connections.models import Connection

# Create your models here.

class Invoice(models.Model):
    invoice_no = models.IntegerField()
    invoice_date = models.DateField()
    products = models.ManyToManyField(Product, through='InvoiceItem')
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10,  decimal_places=2)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    taxable = models.DecimalField(max_digits=10, decimal_places=2)
    cgst = models.DecimalField(max_digits=5, decimal_places=2)
    sgst = models.DecimalField(max_digits=5, decimal_places=2)
    igst = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

