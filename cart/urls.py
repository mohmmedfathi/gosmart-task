from django.urls import path
from .api import CartView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart-view'),
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]
