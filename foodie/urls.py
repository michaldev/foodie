from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.site.site_header = 'Foodie - Panel Admina'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basefood', include('basefood.urls')),
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),
    url(r'^rest-auth/', include('rest_auth.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
