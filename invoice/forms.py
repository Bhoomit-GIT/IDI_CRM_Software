from django import forms
from .models import Invoice, InvoiceItem

class InvoiceModelForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_no', 'invoice_date', 'connection']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'rate', 'taxable', 'cgst', 'sgst', 'igst']