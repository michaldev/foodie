from rest_framework import generics
from .models import Category, Product, Vitamin, Preservative, Contact
from .serializers import \
    CategorySerializer, ProductFullSerializer, \
    ProductSerializer, VitaminSerializer, PreservativeSerializer, ContactSerializer
from rest_framework import filters
#from rest_framework import permissions
#from rest_framework.permissions import IsAuthenticated


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
    #permission_classes = (IsAuthenticated,)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter


class Product(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer


class ContactView(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
