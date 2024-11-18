from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .forms import InvoiceModelForm, InvoiceItemForm
from .models import Invoice, InvoiceItem
from terms_and_conditions.models import Invoice_terms_and_conditions
from django.views import View
from connections.models import Connection
from connections.forms import ConnectionModelForm,ConnectionInvoiceModelForm
from django.http import JsonResponse
from django.db import transaction
from django.urls import reverse
from datetime import date
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .utils import fiscal_number_generator,get_invoice_number,change

InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1)

# def connection_search(request):
#     query = request.GET.get('q')
#     connections = Connection.objects.filter(c_name__icontains=query)
#     results = [{'id': connection.id, 'text': connection.c_name} for connection in connections]
#     return JsonResponse({'results': results})

class InvoiceCreateView(CreateView):
    template_name = 'invoice/invoice_create.html'
    model = Invoice
    form_class = InvoiceModelForm
    success_url = '/invoice/create/'

    def get(self, request, *args, **kwargs):

        invoice_form = InvoiceModelForm(initial={'invoice_no': get_invoice_number(),'invoice_date':date.today()})

        invoice_form.fields['invoice_date'].widget.attrs.update({
            "hx-get": reverse('invoice:get_invoice_number') + "?invoice_date=",
            "hx-trigger": "change delay:0ms",
            'hx-target': '#invoice_no',
            'hx-swap': 'outerHTML'
        })

        invoice_form.fields['connection'].widget.attrs.update({
            "hx-get": reverse('invoice:change'),
            "hx-trigger": "change delay:0ms",
            'hx-target': '#c_name,#c_company_name,#c_GSTIN,#c_mobile_no,#c_email,#c_city,#c_state,#c_country,#c_billing_address,#c_shipping_address',
            'hx-swap': 'outerHTML',
            'id': 'connection_object'
        })



        invoice_item_formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())
        connection_form = ConnectionInvoiceModelForm()
        
        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
            'connection_form': connection_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        invoice_form = InvoiceModelForm(request.POST)
        invoice_item_formset = InvoiceItemFormSet(request.POST) 

        if invoice_form.is_valid() and invoice_item_formset.is_valid():
            try:
                with transaction.atomic():
                    invoice = invoice_form.save(commit=False)
                    invoice.invoice_no = fiscal_number_generator(invoice.invoice_no,invoice.invoice_date)
                    invoice.save()
                    total_amount = 0
                    ab_cgst = 0
                    sgst = 0
                    for item_form in invoice_item_formset:
                        if item_form.cleaned_data:
                            invoice_item = item_form.save(commit=False)
                            invoice_item.invoice = invoice  
                            # invoice_item.amount = invoice_item.quantity * invoice_item.rate
                            # total_amount += invoice_item.amount
                            # ab_cgst += invoice_item.amount  * (invoice_item.cgst/100)
                            invoice_item.save() 
                    # invoice.total = total_amount
                    # invoice.a_cgst = ab_cgst
                    invoice.save() 

                    return redirect(self.success_url)
            except Exception as e:
                print(f"Error saving invoice: {e}")

        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }
        return render(request, self.template_name, context)
    
class InvoiceDetailView(View):
    template_name = 'invoice/invoice_detail.html'

    def get(self, request, id, *args, **kwargs):
        invoice = get_object_or_404(Invoice, id=id)
        invoice_items = InvoiceItem.objects.filter(invoice=invoice)
        terms_and_conditons = Invoice_terms_and_conditions.objects.all()

        context = {
            'invoice': invoice,
            'invoice_items': invoice_items,
            't_and_c': terms_and_conditons,
        }
        return render(request, self.template_name, context)