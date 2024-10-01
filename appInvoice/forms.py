from django import forms
from .models import Product

class rawproduct(forms.Form):
    price =  forms.CharField(max_length=23)

class ProductForm(forms.ModelForm):
    price = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder':'Your Price Product'}))
    class Meta:
        model=Product
        fields=[
            'price'
        ] 