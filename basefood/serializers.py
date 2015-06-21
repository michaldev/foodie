# -*- coding: utf-8 -*-
from rest_framework import serializers
from basefood.models import Category, CategoryMain, Product, Vitamin, Mineral, Preservative, Shop, Price


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
        fields = ('id', 'name', 'othername', 'slug', 'description')


class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mineral
        fields = ('id', 'name', 'slug', 'description')


class PreservativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preservative
        fields = ('id', 'name', 'othername', 'slug', 'description', 'level')


class ShopSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        a = Price.objects.get(product=1, shop=1).price
        return a
    class Meta:
        model = Shop
        fields = ('id', 'name', 'slug', 'image', 'price')


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
            'portion', 'preservatives', 'shops')

