from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryList, Product

urlpatterns = patterns('basefood.views',
    url(
        regex = r'^/category', 
        view = CategoryList.as_view(),
        name = 'basefood-category-list'),                 
    url(
        regex = r'^/(?P<pk>[0-9]+)/$', 
        view = Product.as_view(),
        name = 'basefood-product'),                   
)

urlpatterns = format_suffix_patterns(urlpatterns)