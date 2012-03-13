from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pilka.places.views',
    url( r'^$', 'all', name='all-places' ),
)
