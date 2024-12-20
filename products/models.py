from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=15)
    product_description = models.TextField()
    product_price = models.DecimalField(decimal_places=2,max_digits=15)
    is_deleted = models.BooleanField(default=False)
    product_hsn = models.IntegerField(default=32543)
    

    def get_absolute_url(self):
        return reverse("products:products-detail", kwargs={"id": self.id})
 