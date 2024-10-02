from rest_framework import serializers
from .models import Product, Category, Brand



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (['name','image'])

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (['name','image'])

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

    #StringRelatedField: to return (only) the name of category
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()

    price_with_tax = serializers.SerializerMethodField(method_name='price_tax_calc')
    def price_tax_calc(self, product:Product):
        return product.price * 1.1
