from django import forms
from django.forms.models import inlineformset_factory,modelformset_factory
from .models import Invoice, InvoiceItem

class InvoiceModelForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_no', 'invoice_date', 'connection']


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'rate', 'taxable', 'cgst', 'sgst', 'igst']

InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=0)        

