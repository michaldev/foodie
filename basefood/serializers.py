# -*- coding: utf-8 -*-
from rest_framework import serializers
from basefood.models import \
    Category, CategoryMain, Product, Vitamin, \
    Mineral, Preservative, Shop, Price, Ingredient, Producer


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
            'id', 'name', 'othername', 'slug', 'description', 'level', 'dmax')


class ShopSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        ctx = self.context
        view = ctx['view']
        pid = view.kwargs['slug']
        idProduktu = Product.objects.get(slug=pid).id
        cena = Price.objects.get(product=idProduktu, shop=obj.id).price
        return cena

    class Meta:
        model = Shop
        fields = ('id', 'name', 'slug', 'image', 'price')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'slug', 'allergen', 'gluten')


class ProducerSerializer(serializers.ModelSerializer):
    """Główna serializacja producenta"""
    class Meta:
        model = Producer
        fields = ('id', 'name', 'slug', 'poland_producer')


class ProductSerializer(serializers.ModelSerializer):
    """Główna serializacja produktu"""
    producer = ProducerSerializer()

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
    producer = ProducerSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'producer', 'slug', 'image', 'image2', 'category', 'sugar', 'size',
            'protein', 'vitamins', 'minerals', 'carbohydrates', 'fats', 'fatsSaturated', 'energyValue', 
            'portion', 'preservatives', 'shops', 'ingredients')

