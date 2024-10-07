from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice_no = models.IntegerField()
    invoice_date = models.DateField()
    p_qty = models.IntegerField()
    p_unit = models.TextChoices()
    p_rate = models.IntegerField()
    