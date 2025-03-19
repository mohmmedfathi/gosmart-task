from django.urls import path
from .api import PlaceOrderView, OrderHistoryView

urlpatterns = [
    path('place/', PlaceOrderView.as_view(), name='place-order'),
    path('history/', OrderHistoryView.as_view(), name='order-history'),
]
