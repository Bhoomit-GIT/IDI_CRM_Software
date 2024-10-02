from django.urls import path
from .views import (
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    MyListView,
    ProductDetailView
)


app_name = 'products'
urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='products-create'),
    path('<int:id>/update/', ProductUpdateView.as_view(), name='products-update'),
    path('<int:id>/delete/', ProductDeleteView.as_view(), name='products-delete'),
    path('', MyListView.as_view(), name='products-list'),
    path('<int:id>/', ProductDetailView.as_view(), name='products-detail'),
] 