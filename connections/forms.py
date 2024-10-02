from django import forms
from .models import Connection

class ConnectionModelForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = [
            'c_name',
            'c_company_name',
            'c_mobile_no',
            'c_email',
            'c_website',
            'c_industry',
            'c_segment',
            'c_city',
            'c_state',
            'c_country',
            'c_billing_address',
            'c_shipping_address',
            'c_connection_type',
            'c_GSTIN',
            'cbd_bank_name',
            'cbd_branch',
            'cbd_account_no',
            'cbd_ifsc',
            'cbd_swift_code'
        ]       