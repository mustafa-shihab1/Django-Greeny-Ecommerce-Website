from rest_framework import serializers
from .models import Product, Category, Brand



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (['name','image'])


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

# StringRelatedField: to return (only) the name of category
    category = serializers.StringRelatedField()
    brand = BrandSerializer()

    price_with_tax = serializers.SerializerMethodField(method_name='price_tax_calc')

    def price_tax_calc(self, product:Product):
        return product.price * 1.1

# this function will be executed in api.py when using -> serializer.is_valid(..)
    # def validate(self, data):
    #     if data['password1'] != data['password2']:
    #         return serializers.ValidationError('RETURN TEXT ERROR!')
