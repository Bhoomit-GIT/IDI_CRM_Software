from django.urls import path
from .views import InvoiceCreateView, InvoiceDetailView

app_name = 'invoice'

urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    # path('add-product/', add_product, name='add-product'),
    path('<int:id>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]