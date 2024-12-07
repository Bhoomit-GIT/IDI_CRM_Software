from datetime import date
from django.http import HttpResponse
from datetime import datetime
from django.forms import modelformset_factory
from .forms import InvoiceModelForm, InvoiceItemForm
from .models import Invoice
from .models import Invoice, InvoiceItem
from django.shortcuts import render, redirect, get_object_or_404
from connections.models import Connection
from django.template.loader import render_to_string
from django.http import JsonResponse
from django import forms

from connections.forms import ConnectionInvoiceModelForm,ConnectionModelForm
from .forms import Invoice_no_modelform

InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1)
def get_gst_type_view(request):
    gstin = request.GET.get('c_GSTIN', '')
    # Logic to determine CGST/SGST or IGST based on GSTIN.
    gst_type = "cgst_sgst" if gstin.startswith('24') else "igst"  # Replace with actual logic.
    context = {
        'gst_type': gst_type,
        'gst_fields.html':'invoice/gst_fields.html'
    }
    return HttpResponse(context)


def change_connection(request):
    connection_id = request.GET.get('connection')  
    if not connection_id:
        return JsonResponse({'error': 'Connection ID not provided'}, status=400)
    try:
        connection_instance = Connection.objects.get(id=connection_id)
        connection_form = ConnectionInvoiceModelForm(instance=connection_instance)
        gstin = connection_instance.c_GSTIN
        gst_type = "cgst_sgst" if gstin.startswith('24') else "igst" 

        # Render the appropriate fields based on GST type
        context = {
            'connection_form': connection_form,
            'gst_type': gst_type,
            'invoice_item_formset': InvoiceItemFormSet(queryset=InvoiceItem.objects.none())  # Pass an empty formset
        }
        html = render_to_string('gst_fields.html', context)  # Render the fields to HTML
        return HttpResponse(connection_form.as_p())  # Return the rendered HTML
    except Connection.DoesNotExist:
        return JsonResponse({'error': 'Connection not found'}, status=404)


def fiscal_number_generator(invoice_no,selected_date):
    year = selected_date.year
    if selected_date.month < 4:
        fiscal_year = f"{year - 1}-{year}" 
    else: 
        fiscal_year = f"{year}-{year + 1}"
    return f"IDI - {fiscal_year} - {invoice_no}"

def get_invoice_number(request=None):
    date_str = request.GET.get('invoice_date') if request else None
    
    if date_str:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        selected_date = date.today()

    year = selected_date.year
    if selected_date.month < 4:
        fiscal_year = f"{year - 1}-{year}" 
    else:
        fiscal_year = f"{year}-{year + 1}"    

    invoices = Invoice.objects.filter(invoice_no__contains=f"IDI - {fiscal_year}").order_by("invoice_no")
    existing_numbers = []
    for invoice in invoices:
        try:
            number = int(invoice.invoice_no.split(" - ")[-1])
            existing_numbers.append(number)
        except ValueError:
            continue
    next_number = 1
    for i, number in enumerate(sorted(existing_numbers), start=1):
        if number != i:
            next_number = i
            break
    else:
        next_number = len(existing_numbers) + 1
        
    new_invoice_no = f"{next_number:03d}"
    invoice_form = Invoice_no_modelform(initial={'invoice_no': new_invoice_no})
    if request:
        return HttpResponse(invoice_form)
    else:
        return new_invoice_no





























# def generator_invoice_number(request):
#     date = request.GET.get('invoice_date')
#     if date:
#         selected_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
#     else:
#         selected_date = datetime.date.today()
#     year = selected_date.year
#     if selected_date.month < 4:
#         fiscal_year = f"{year - 1}-{year}"
#     else:
#         fiscal_year = f"{year}-{year + 1}"
#     last_invoice = Invoice.objects.filter(fiscal_year=fiscal_year).order_by("number").last()
#     next_number = last_invoice.number + 1 if last_invoice else 1
#     invoice_no = f"ID2343I - {fiscal_year} - {next_number:03d}"
#     return JsonResponse({"invoice_no": invoice_no})            
 

# def generator_invoice_number(invoice_date):
#     year = invoice_date.year
#     month = invoice_date.month
#     current_year = invoice_date.year
#     if invoice_date.month < 4:
#             fiscal_start_year = current_year - 1
#     else:
#             fiscal_start_year = current_year
#     # all_ids = list(Invoice.objects.filter(invoice_no__contains=f"{fiscal_start_year}-{fiscal_start_year+1}").order_by('invoice_no').values_list('invoice_no', flat=True))
#     all_ids = list(Invoice.objects.values_list('id', flat=True))
#     new_id = 1 
#     while new_id in all_ids:
#             new_id += 1
        
#     return f"{new_id:02}"

# def fiscal_year_range_generator(invoice_no,invoice_date):
#         current_year = invoice_date.year
#         if invoice_date.month < 4:
#                 fiscal_start_year = current_year - 1
#         else:
#                 fiscal_start_year = current_year
        
#         fiscal_year_range = f"{fiscal_start_year}/{str(fiscal_start_year + 1)[-2:]}"     

#         return f"IDI {fiscal_year_range} - {invoice_no}"   

# def generator_invoice_number(invoice_date):
#     year = invoice_date.year
#     month = invoice_date.month

#     if month >= 4:
#         fiscal_year_start = year
#         fiscal_year_end = year + 1
#     else:
#         fiscal_year_start = year - 1
#         fiscal_year_end = year

#     # Check for the last invoice in the current fiscal year
#     last_invoice = Invoice.objects.filter(
#         invoice_no__contains=f"{fiscal_year_start}-{fiscal_year_end}"
#     ).order_by('invoice_no').last()

#     if last_invoice:
#         last_invoice_number = int(last_invoice.invoice_no.split(" - ")[-1])
#         new_invoice_number = last_invoice_number + 1
#     else:
#         new_invoice_number = 1

#     invoice_no = f"IDI - {fiscal_year_start}-{fiscal_year_end} - {new_invoice_number:03d}"
#     return invoice_no