from django.urls import path
from .views import InvoiceCreateView, InvoiceDetailView

app_name = 'invoice'

urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]