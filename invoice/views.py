from django.shortcuts import render,redirect
from .models import Invoice,InvoiceItem
from django.views import View
from .forms import InvoiceItemFormSet,InvoiceModelForm

# Create your views here.

class InvoiceCreateView(View):
    template_name = 'invoice/invoice_create.html'  # Define the template where the form will be rendered

    def get(self, request, *args, **kwargs):
        # Handle GET request (displaying an empty form)
        invoice_form = InvoiceModelForm()
        invoice_item_formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())  # Empty formset for new items
        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Handle POST request (form submission)
        invoice_form = InvoiceModelForm(request.POST)
        invoice_item_formset = InvoiceItemFormSet(request.POST)

        if invoice_form.is_valid() and invoice_item_formset.is_valid():
            # Save the invoice
            invoice = invoice_form.save()

            # Save the invoice items (but don't commit them yet, to set the foreign key)
            invoice_items = invoice_item_formset.save(commit=False)
            for item in invoice_items:
                item.invoice = invoice  # Assign the invoice foreign key
                item.save()

            # Redirect to a success page or another relevant view
            return redirect('/invoices/create')

        # If the form is not valid, re-render the form with validation errors
        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }
        return render(request, self.template_name, context)