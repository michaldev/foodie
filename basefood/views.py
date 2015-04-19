from rest_framework import generics
from .models import Category, CategoryMain
from .serializers import CategorySerializer, CategoryMainSerializer
from django.views.generic import TemplateView

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryMainList(generics.ListCreateAPIView):
    queryset = CategoryMain.objects.all()
    serializer_class = CategoryMainSerializer