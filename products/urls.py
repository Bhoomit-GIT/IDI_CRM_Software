from django.urls import path
from .views import (
    ProductDetailView,
    MyListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)


app_name = 'products'
urlpatterns = [
    path('<int:id>/', ProductDetailView.as_view(), name='products-detail'),
    path('', MyListView.as_view(), name='products-list'),
    path('create/', ProductCreateView.as_view(), name='products-create'),
    path('<int:id>/update/', ProductUpdateView.as_view(), name='products-update'),
    path('<int:id>/delete/', ProductDeleteView.as_view(), name='products-delete'),
]