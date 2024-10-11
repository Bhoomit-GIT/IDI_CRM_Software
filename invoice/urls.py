from django.urls import path
from .views import (
    InvoiceCreateView
)


app_name = 'invoice'
urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='invoices-create'),
    # path('<int:id>/update/', ProductUpdateView.as_view(), name='products-update'),
    # path('<int:id>/delete/', ProductDeleteView.as_view(), name='products-delete'),
    # path('', MyListView.as_view(), name='products-list'),
    # path('<int:id>/', ProductDetailView.as_view(), name='products-detail'), 
] 