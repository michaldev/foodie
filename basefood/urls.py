from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryList, Product, VitaminList, PreservativeList, ProductList

urlpatterns = patterns('basefood.views',
    url(
        regex = r'^/category', 
        view = CategoryList.as_view(),
        name = 'basefood-category-list'),
    url(
        regex = r'^/vitamins', 
        view = VitaminList.as_view(),
        name = 'basefood-vitamin-list'),
    url(
        regex = r'^/products', 
        view = ProductList.as_view(),
        name = 'basefood-product-list'),
    url(
        regex = r'^/preservatives', 
        view = PreservativeList.as_view(),
        name = 'basefood-preservative-list'),
    url(
        regex = r'^/(?P<pk>[0-9]+)/$', 
        view = Product.as_view(),
        name = 'basefood-product'),
)

urlpatterns = format_suffix_patterns(urlpatterns)