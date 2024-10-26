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
        fields = ['product', 'quantity', 'rate', 'taxable', 'cgst', 'sgst', 'igst', 'amount']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'taxable': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'cgst': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'sgst': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'igst': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
        }

