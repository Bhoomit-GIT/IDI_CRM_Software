from django.db import models


# Create your models here.

class Connection(models.Model):
    c_name             = models.CharField(max_length=10)    # c - connection
    c_company_name     = models.CharField(max_length=15)
    c_mobile_no        = models.IntegerField()
    c_email            = models.EmailField(null=True)
    c_website          = models.URLField(null=True)
    c_industry         = models.CharField(null=True,max_length=10)
    c_segment          = models.CharField(null=True,max_length=10)
    c_city             = models.CharField(max_length=10)
    c_state            = models.CharField(max_length=10)
    c_country          = models.CharField(max_length=10)
    c_billing_address  = models.TextField()
    c_shipping_address = models.TextField()
    c_connection_type  = models.CharField(max_length=10)
    c_GSTIN            = models.CharField(max_length=15)
    cbd_bank_name      = models.CharField(max_length=10)    # cbd - connection bank details
    cbd_branch         = models.CharField(max_length=10)
    cbd_account_no     = models.IntegerField()
    cbd_ifsc           = models.CharField(max_length=10)
    cbd_swift_code     = models.CharField(max_length=10)
    

    # def __str__(self):
    #     return self.c_name  # This ensures that the name will be shown in the dropdown
    
    