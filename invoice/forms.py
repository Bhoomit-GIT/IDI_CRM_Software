from django import forms
from .models import Invoice, InvoiceItem


class InvoiceModelForm(forms.ModelForm):
    invoice_no = forms.CharField(max_length=255, required=False) 
    class Meta:
        model = Invoice
        fields = ['invoice_no', 'invoice_date', 'connection']

        def __init__(self, *args, **kwargs):
            invoice_no = kwargs.pop('invoice_no', None)  
            super().__init__(*args, **kwargs)
            if invoice_no:
                self.fields['invoice_no'].initial = invoice_no 

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'rate', 'taxable', 'cgst', 'sgst', 'igst']