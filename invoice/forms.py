from django import forms
from django.forms import inlineformset_factory
from .models import Invoice,InvoiceItem

class InvoiceModelForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoice_no',
            'invoice_date',
            'connection'
        ]    

class InvoiceItemModelForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem    
        fields = [
            'product',
            'quantity',
            'rate',
            'taxable',
            'cgst',
            'sgst'
        ]    

InvoiceItemFormSet = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemModelForm, extra=1)        
