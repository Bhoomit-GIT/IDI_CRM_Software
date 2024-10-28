from django.db import models
from products.models import Product
from connections.models import Connection
from django.urls import reverse

class Invoice(models.Model):
    invoice_no = models.IntegerField(unique=True)  # Unique invoice number
    invoice_date = models.DateField()
    products = models.ManyToManyField(Product, through='InvoiceItem')
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00,null=True, blank=True)

    # def __str__(self):
    #     return f"Invoice {self.invoice_no}"

    # def get_absolute_url(self):
    #     return reverse('invoice:invoice-detail', kwargs={'id': self.pk})


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    taxable = models.DecimalField(max_digits=10, decimal_places=2, default=3.00)
    cgst = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)
    sgst = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)
    igst = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=3.00)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.rate
        super().save(*args, **kwargs)