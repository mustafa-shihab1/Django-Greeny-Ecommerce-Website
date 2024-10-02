from rest_framework import serializers
from .models import Product, Category, Brand, Review



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

    price_with_tax = serializers.SerializerMethodField(method_name='price_tax_calc')
    def price_tax_calc(self, product:Product):
        return product.price * 1.1



class BrandSerializerDetail(serializers.ModelSerializer):
    products = ProductSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = (['name','image','products'])

class CategorySerializerDetail(serializers.ModelSerializer):
    products = ProductSerializer(source='product_category', many=True)
    class Meta:
        model = Category
        fields = (['name','image','products'])


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = (['user','rate','review'])


class ProductSerializerDetail(serializers.ModelSerializer):
    reviews = ReviewSerializer(source='product_review', many=True)
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = (['name','image','price','flag','category','brand','reviews'])
