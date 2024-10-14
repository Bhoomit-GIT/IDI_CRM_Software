# forms.py in the invoice app
from django import forms
from django.forms import modelformset_factory
from .models import Invoice, InvoiceItem

class InvoiceModelForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_no', 'invoice_date', 'connection']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'rate', 'taxable', 'cgst', 'sgst', 'igst','amount']
        
InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1, can_delete=True)
