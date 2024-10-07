from django import forms
from .models import Invoice

class InvoiceModelForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoice_no',
            'invoice_date'
        ]    
