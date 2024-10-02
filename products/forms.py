from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_description',
            'product_price'
        ]
    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if product_name.lower() == 'abc':
            raise forms.ValidationError("This is not a valid name for product")    
        return product_name 