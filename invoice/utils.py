import datetime
from datetime import date
from .models import Invoice

def generator_invoice_number():
        current_year = date.today().year
        if date.today().month < 4:
            fiscal_start_year = current_year - 1
        else:
            fiscal_start_year = current_year
        fiscal_year_range = f"{fiscal_start_year}/{str(fiscal_start_year + 1)[-2:]}"
        last_invoice_number = Invoice.objects.last().invoice_no.split(" - ")[-1] if Invoice.objects.exists() else "0001"
        new_invoice_number = str(int(last_invoice_number) + 1).zfill(2)
        return f"IDI {fiscal_year_range} - {new_invoice_number}"
