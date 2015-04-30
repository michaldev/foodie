from rest_framework import generics
from .models import Category, Product, Vitamin, Preservative
from .serializers import CategorySerializer, ProductSerializer, VitaminSerializer, PreservativeSerializer
from django.views.generic import TemplateView


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VitaminList(generics.ListCreateAPIView):
    queryset = Vitamin.objects.all()
    serializer_class = VitaminSerializer


class PreservativeList(generics.ListCreateAPIView):
    queryset = Preservative.objects.all()
    serializer_class = PreservativeSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
