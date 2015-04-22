# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Category, CategoryMain, Product, Vitamin, Mineral, Preservative, Shop


class CategoryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMain
        fields = ('id', 'name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    """Główna serializacja kategorii"""
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


class PreservativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preservative
        fields = ('id', 'name', 'slug', 'description', 'level')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'slug', 'image')


class ProductSerializer(serializers.ModelSerializer):
    """Główna serializacja produktu"""
    category = CategorySerializer(many=True, read_only=True)
    vitamins = VitaminSerializer(many=True, read_only=True)
    minerals = MineralSerializer(many=True, read_only=True)
    preservatives = PreservativeSerializer(many=True, read_only=True)
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'producer', 'slug', 'image', 'image2', 'category', 'sugar', 'size',
            'protein', 'vitamins', 'minerals', 'carbohydrates', 'fats', 'fatsSaturated', 'energyValue', 
            'portion', 'preservatives', 'shops', 'pricemin', 'pricemax')
