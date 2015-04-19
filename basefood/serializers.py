from rest_framework import serializers
from .models import Category, CategoryMain

class CategorySerializer(serializers.ModelSerializer):
    categorymain = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'categorymain')

class CategoryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMain
        fields = ('id', 'name', 'slug')