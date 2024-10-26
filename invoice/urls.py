from django.urls import path
from .views import InvoiceCreateView, add_product, InvoiceDetailView

app_name = 'invoice'

urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('add-product/', add_product, name='add_product'),
    path('<int:id>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]