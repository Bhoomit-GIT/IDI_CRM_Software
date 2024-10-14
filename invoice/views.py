# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.forms import modelformset_factory
from .forms import InvoiceModelForm, InvoiceItemForm
from .models import Invoice, InvoiceItem

class InvoiceCreateView(View):
    template_name = 'invoice/invoice_create.html'

    def get(self, request, *args, **kwargs):
        invoice_form = InvoiceModelForm()
        InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1)
        invoice_item_formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())

        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        invoice_form = InvoiceModelForm(request.POST)
        InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1)
        invoice_item_formset = InvoiceItemFormSet(request.POST)

        if invoice_form.is_valid() and invoice_item_formset.is_valid():
            invoice = invoice_form.save()  # Save the invoice first
            for item_form in invoice_item_formset:
                invoice_item = item_form.save(commit=False)
                invoice_item.invoice = invoice  # Associate item with invoice
                invoice_item.save()

            return redirect('invoice_detail', pk=invoice.pk)

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

        context = {
            'invoice': invoice,
            'invoice_items': invoice_items,
        }
        return render(request, self.template_name, context)