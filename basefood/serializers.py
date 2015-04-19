from rest_framework import serializers
from .models import Category, CategoryMain, Product, Vitamin, Mineral

class CategoryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMain
        fields = ('id', 'name', 'slug')

class CategorySerializer(serializers.ModelSerializer):
    categorymain = CategoryMainSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'categorymain')

class VitaminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamin
        fields = ('id', 'name', 'slug', 'description')

class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mineral
        fields = ('id', 'name', 'slug', 'description')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    vitamins = VitaminSerializer(many=True, read_only=True)
    minerals = MineralSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'producer', 'slug', 'image', 'image2', 'category', 'sugar', 'size',
        	'protein', 'vitamins', 'minerals', 'carbohydrates', 'fats', 'fatsSaturated', 'energyValue', 
        	'portion', 'preservatives', 'shops', 'pricemin', 'pricemax')