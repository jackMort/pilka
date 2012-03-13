from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url( r'^$', 'pilka.views.index', name='index' ),

    url( r'^admin/', include( admin.site.urls ) ),
    url( r'^places/$', include( 'pilka.places.urls' ) ),
)

urlpatterns +=staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns = patterns ( '',
        url( r'^' + settings.MEDIA_URL.lstrip( '/' ), include( 'appmedia.urls' ) ),
    ) + urlpatterns
