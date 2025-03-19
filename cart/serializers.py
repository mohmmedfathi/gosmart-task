from rest_framework import serializers
from .models import Cart, CartItem
from product.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']

    def create(self, validated_data):
        user = self.context['request'].user
        product = Product.objects.filter(id=validated_data['product_id']).first()

        if not product:
            raise serializers.ValidationError({"error": "Product not found."})

        cart, _ = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        cart_item.quantity = cart_item.quantity + validated_data['quantity'] if not created else validated_data['quantity']
        cart_item.save()
        return cart_item

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()
