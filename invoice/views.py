from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.http import JsonResponse
from .forms import InvoiceModelForm, InvoiceItemForm
from .models import Invoice, InvoiceItem
from terms_and_conditions.models import Invoice_terms_and_conditions
from django.views import View
from django.db import transaction
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .utils import generator_invoice_number

InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1)

class InvoiceCreateView(CreateView):
    template_name = 'invoice/invoice_create.html'
    model = Invoice
    form_class = InvoiceModelForm
    success_url = '/invoice/create/'


    def get(self, request, *args, **kwargs):
        invoice_no = generator_invoice_number() 
        invoice_form = InvoiceModelForm(initial={'invoice_no': invoice_no})
        invoice_item_formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())


        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        invoice_form = InvoiceModelForm(request.POST)
        invoice_item_formset = InvoiceItemFormSet(request.POST) 

        if invoice_form.is_valid() and invoice_item_formset.is_valid():
            try:
                with transaction.atomic():
                    invoice = invoice_form.save()
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