# models.py in the invoice app
from django.db import models
from products.models import Product
from connections.models import Connection
from django.urls import reverse

class Invoice(models.Model):
    invoice_no = models.IntegerField(unique=True)  # Make invoice_no unique
    invoice_date = models.DateField()
    products = models.ManyToManyField(Product, through='InvoiceItem')
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    # total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  # Default value
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Invoice {self.invoice_no}"
    
    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'pk': self.pk})

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # Linked to Invoice
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Linked to Product
    quantity = models.PositiveIntegerField(default=1)  # Default to 1 
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    taxable = models.DecimalField(max_digits=10, decimal_places=2, default=3.00)  # Default value
    cgst = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)  # Default value
    sgst = models.DecimalField(max_digits=5, decimal_places=2, default=3.00)  # Default value
    igst = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=3.00)  # Default value
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     # Calculate the amount based on quantity and rate
    #     self.amount = self.quantity * self.rate
    #     super().save(*args, **kwargs)  # Call the original save method



