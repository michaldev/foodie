from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from main.views import Homepage



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(
	    regex = r'^$', 
	    view = Homepage.as_view(),
	    name = 'home'),
    url(r'^basefood', include('basefood.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()