from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    price_with_tax = serializers.SerializerMethodField(method_name='price_tax_calc')

    def price_tax_calc(self, product:Product):
        return product.price * 1.1

    class Meta:
        model = Product
        fields = ('__all__')