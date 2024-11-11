from django import forms
from .models import Invoice, InvoiceItem

class InvoiceModelForm(forms.ModelForm):
    invoice_no = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'id': 'invoice_no'}) )
    invoice_date = forms.DateField(widget=forms.DateInput(attrs={'id': 'invoice_date','type': 'date'}))
    class Meta:
        model = Invoice 
        fields = ['invoice_no', 'invoice_date', 'connection']

class Invoice_no_modelform(forms.ModelForm):
    invoice_no = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'id': 'invoice_no'}) )
    class Meta:
        model = Invoice 
        fields = ['invoice_no']        

class InvoiceItemForm(forms.ModelForm):
    class Meta: 
        model = InvoiceItem
        fields = ['product', 'quantity', 'rate', 'taxable', 'cgst', 'sgst', 'igst']