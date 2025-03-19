from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from product.models import Product
from .serializers import CartSerializer, CartItemSerializer

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class RemoveFromCartView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()  
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) 