from rest_framework import serializers
from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'
