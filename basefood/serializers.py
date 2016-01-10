# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.db.models import Max, Min
from basefood.models import \
    Category, CategoryMain, Product, Vitamin, \
    Mineral, Preservative, Shop, Ingredient, Producer, Contact


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
        fields = (
            'id', 'name', 'othername', 'slug', 'description', 'dmax', 'level')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'slug', 'image')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'slug', 'allergen', 'gluten')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'mail', 'title', 'type', 'description')


class ProducerSerializer(serializers.ModelSerializer):
    """Główna serializacja producenta"""
    class Meta:
        model = Producer
        fields = ('id', 'name', 'slug', 'local_producer')


class ProductSerializer(serializers.ModelSerializer):
    """Główna serializacja produktu"""
    producer = ProducerSerializer(many=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'producer', 'slug', 'image')


class ProductFullSerializer(serializers.ModelSerializer):
    """Główna serializacja pełnego produktu"""
    category = CategorySerializer(many=True, read_only=True)
    vitamins = VitaminSerializer(many=True, read_only=True)
    minerals = MineralSerializer(many=True, read_only=True)
    preservatives = PreservativeSerializer(many=True, read_only=True)
    shops = ShopSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    producer = ProducerSerializer(many=False, read_only=True)
    values_category = serializers.SerializerMethodField()
    values_calculated = serializers.SerializerMethodField()

    def get_values_category(self, obj):
        return Product.objects.filter(
            category=obj.category.all()).aggregate(
            Min('fats'),
            Max('fats'),
            Min('sugar'),
            Max('sugar'),
            Min('protein'),
            Max('protein'),
            )

    def get_values_calculated(self, obj):
        protein_max = self.get_values_category(obj)['protein__max']
        fats_max = self.get_values_category(obj)['fats__max']
        sugar_max = self.get_values_category(obj)['sugar__max']
        data = {
            'protein': '%.2f' % (obj.protein*100/protein_max),
            'sugar': '%.2f' % (obj.sugar*100/sugar_max),
            'fats': '%.2f' % (obj.fats*100/fats_max)
        }
        return data

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'producer', 'slug',
            'image', 'image2', 'category', 'sugar',
            'size', 'protein', 'vitamins', 'minerals',
            'carbohydrates', 'fats', 'fatsSaturated', 'energyValue',
            'portion', 'preservatives', 'shops', 'ingredients',
            'values_category', 'values_calculated')

