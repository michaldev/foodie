from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryList, CategoryMainList

urlpatterns = patterns('basefood.views',
    url(
        regex = r'^/category', 
        view = CategoryList.as_view(),
        name = 'basefood-category-list'),                 
    url(
        regex = r'^/catmain', 
        view = CategoryMainList.as_view(),
        name = 'basefood-category-main-list'),                       
)

urlpatterns = format_suffix_patterns(urlpatterns)