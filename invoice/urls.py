from django.urls import path
from .views import InvoiceCreateView, InvoiceDetailView
from .utils import get_invoice_number,change_connection,get_gst_type_view

from . import views

app_name = 'invoice'

urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:id>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('get_invoice_number/', get_invoice_number, name='get_invoice_number'),
    path('change/', change_connection, name='change'),
    path('get-gst-type/', get_gst_type_view, name='get_gst_type'),
    # path('connection_search',connection_search,name='connection_search')
    
    ]