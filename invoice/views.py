from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.http import JsonResponse
from .forms import InvoiceModelForm, InvoiceItemForm
from .models import Invoice, InvoiceItem
from django.views import View
from django.db import transaction
from django.views.generic.edit import CreateView

InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1)

class InvoiceCreateView(CreateView):
    template_name = 'invoice/invoice_create.html'
    model = Invoice
    form_class = InvoiceModelForm
    success_url = '/invoice/create/'

    def get(self, request, *args, **kwargs):
        invoice_form = self.get_form()
        invoice_item_formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())

        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        invoice_form = InvoiceModelForm(request.POST)
        invoice_item_formset = InvoiceItemFormSet(request.POST)  # Ensure all formset data is captured

        if invoice_form.is_valid() and invoice_item_formset.is_valid():
            try:
                with transaction.atomic():
                    invoice = invoice_form.save()

                    total_amount = 0

                    # Loop through all the forms in the formset
                    for item_form in invoice_item_formset:
                        if item_form.cleaned_data and not item_form.cleaned_data.get('DELETE'):
                            invoice_item = item_form.save(commit=False)
                            invoice_item.invoice = invoice  # Link the item to the newly created invoice
                            invoice_item.amount = invoice_item.quantity * invoice_item.rate
                            total_amount += invoice_item.amount
                            invoice_item.save()  # Save each individual invoice item to the DB

                    # Update the total amount for the invoice
                    invoice.total = total_amount
                    invoice.save()

                    return redirect(self.success_url)
            except Exception as e:
                print(f"Error saving invoice: {e}")

        # If forms are invalid, render again with errors
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


def add_product(request):
    formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())
    new_form = formset.empty_form
    # Dynamically set the prefix to handle multiple forms properly
    new_form.prefix = f"invoiceitem_set-{request.GET.get('form_count')}"
    return render(request, 'invoice/invoice_item_form_partial.html', {'form': new_form})