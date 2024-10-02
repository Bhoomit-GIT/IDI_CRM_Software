from django.urls import path
from .views import (
    ConnectionCreateView,
    ConnectionUpdateView,
    ConnectionDeleteView,
    MyListView,
    ConnectionDetailView
)


app_name = 'connections'
urlpatterns = [
    path('create/', ConnectionCreateView.as_view(), name='connections-create'),
    path('<int:id>/update/', ConnectionUpdateView.as_view(), name='connections-update'),
    path('<int:id>/delete/', ConnectionDeleteView.as_view(), name='connections-delete'),
    path('', MyListView.as_view(), name='connections-list'),
    path('<int:id>/', ConnectionDetailView.as_view(), name='connections-detail'),
] 