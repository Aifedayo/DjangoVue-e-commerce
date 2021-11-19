from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'price',
            'product',
            'quantity',
        )
