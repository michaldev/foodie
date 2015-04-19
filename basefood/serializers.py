from rest_framework import serializers
from .models import Category, CategoryMain, Product

class CategoryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMain
        fields = ('id', 'name', 'slug')

class CategorySerializer(serializers.ModelSerializer):
    categorymain = CategoryMainSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'categorymain')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'producer', 'slug', 'image', 'image2', 'category', 'sugar', 'size',
        	'protein', 'vitamins', 'minerals', 'carbohydrates', 'fats', 'fatsSaturated', 'energyValue', 
        	'portion', 'preservatives', 'shops', 'pricemin', 'pricemax')