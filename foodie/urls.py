from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from main.views import \
    Homepage, ProductView, VitaminsView, \
    PreservativeView, HomeView, AboutView, CategoryView, BugdialogView

admin.site.site_header = 'Foodie - Panel Admina'


urlpatterns = patterns('',
    url(
        r'^admin/', include(admin.site.urls)),
    url(
        regex = r'^$',
        view = Homepage.as_view(),
        name = 'home'),
    url(
        r'^basefood', include('basefood.urls')),
    url(
        r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(
        r'^productview', 
        view = ProductView.as_view()
        ),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(
        r'^views/vitamins',
        view = VitaminsView.as_view()
        ),
    url(
        r'^views/home',
        view = HomeView.as_view()
        ),
    url(
        r'^aboutview',
        view = AboutView.as_view()
        ),
    url(
        r'^bugdialogview',
        view = BugdialogView.as_view()
        ),

    url(
        r'^preservativeview',
        view = PreservativeView.as_view()
        ),
    url(
        r'^categoryview',
        view = CategoryView.as_view()
        ),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
