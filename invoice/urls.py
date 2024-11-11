from django.urls import path
from .views import InvoiceCreateView, InvoiceDetailView
from .utils import get_invoice_number

from . import views

app_name = 'invoice'

urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:id>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('get_invoice_number/', get_invoice_number, name='get_invoice_number'),
    # path('connection_search',connection_search,name='connection_search')
    ]