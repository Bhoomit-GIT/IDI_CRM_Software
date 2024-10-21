from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .forms import InvoiceModelForm, InvoiceItemFormSet
from .models import Invoice, InvoiceItem
from django.views import View
from django.db import transaction
from django.views.generic.edit import CreateView

class InvoiceCreateView(CreateView):
    template_name = 'invoice/invoice_create.html'
    model = Invoice
    form_class = InvoiceModelForm
    success_url = '/invoice/create/'  # Redirect to the same page after successful form submission

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
        invoice_item_formset = InvoiceItemFormSet(request.POST)

        if invoice_form.is_valid() and invoice_item_formset.is_valid():
            try:
                with transaction.atomic():
                    invoice = invoice_form.save()  # Save the invoice first

                    # Initialize total amount
                    total_amount = 0

                    for item_form in invoice_item_formset:
                        if item_form.cleaned_data and not item_form.cleaned_data.get('DELETE'):
                            invoice_item = item_form.save(commit=False)
                            invoice_item.invoice = invoice  # Associate the item with the invoice

                            # Calculate item amount
                            quantity = item_form.cleaned_data.get('quantity')
                            rate = item_form.cleaned_data.get('rate')
                            invoice_item.amount = quantity * rate if quantity and rate else 0
                            
                            total_amount += invoice_item.amount  # Add to total amount
                            invoice_item.save()  # Save the item

                    # Update the total amount for the invoice
                    invoice.total = total_amount
                    invoice.save()  # Save the updated invoice

                    return redirect(self.success_url)

            except Exception as e:
                print(f"Error saving invoice: {e}")

        # If either form is invalid, render the form again with errors
        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }
        return render(request, self.template_name, context)

class InvoiceDetailView(View):
    template_name = 'invoice/invoice_detail.html'

    from django.shortcuts import get_object_or_404
from django.views import View

class InvoiceDetailView(View):
    template_name = 'invoice/invoice_detail.html'

    def get(self, request, id, *args, **kwargs):
        print(f"Received id: {id}")  # Debug statement to check the received id
        invoice = get_object_or_404(Invoice, id=id)
        invoice_items = InvoiceItem.objects.filter(invoice=invoice)

        context = {
            'invoice': invoice,
            'invoice_items': invoice_items,
        }
        return render(request, self.template_name, context)
        