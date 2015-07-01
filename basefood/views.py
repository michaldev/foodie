from rest_framework import generics
from .models import Category, Product, Vitamin, Preservative
from .serializers import \
    CategorySerializer, ProductFullSerializer, \
    ProductSerializer, VitaminSerializer, PreservativeSerializer
from rest_framework import filters


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['id', 'slug', 'category', 'sugar']


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('slug', 'name')


class VitaminList(generics.ListCreateAPIView):
    queryset = Vitamin.objects.all()
    serializer_class = VitaminSerializer


class PreservativeList(generics.ListCreateAPIView):
    queryset = Preservative.objects.all()
    serializer_class = PreservativeSerializer


class ProductSearch(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('slug', 'name')


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter


class Product(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
