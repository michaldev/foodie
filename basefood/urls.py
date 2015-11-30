from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryList, Product, VitaminList, PreservativeList, ProductList, ProductSearch, ContactView

urlpatterns = patterns('basefood.views',
    url(
        regex = r'^/category$', 
        view = CategoryList.as_view(),
        name = 'basefood-category-list'),
    url(
        regex = r'^/vitamins$', 
        view = VitaminList.as_view(),
        name = 'basefood-vitamin-list'),
    url(
        regex = r'^/products$', 
        view = ProductList.as_view(),
        name = 'basefood-product-list'),
    url(
        regex = r'^/productsearch$', 
        view = ProductSearch.as_view(),
        name = 'basefood-product-search'),
    url(
        regex = r'^/preservatives$', 
        view = PreservativeList.as_view(),
        name = 'basefood-preservative-list'),
    url(
        regex = r'^/product/(?P<slug>[\w-]+)',
        view = Product.as_view(),
        name = 'basefood-product'),
    url(
        regex = r'^/contact$',
        view = ContactView.as_view(),
        name = 'basefood-product-list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)