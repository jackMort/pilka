from django.db import models
from django.contrib import admin

from googlemaps import GoogleMaps
# TODO: move to settings
GOOGLE_MAP_API_KEY = 'AIzaSyAjgVE1XiMt8iIu318wohPa5-j-qaOOxnM'
gmaps = GoogleMaps( GOOGLE_MAP_API_KEY )


class Type( models.Model ):
    name = models.CharField( max_length=150 )
    codename = models.CharField( max_length=100 )
    description = models.TextField( blank=True, null=True )


class Place( models.Model ):
    type = models.ForeignKey( Type )

    title = models.CharField( max_length=150, blank=True, null=True )
    description = models.TextField( blank=True, null=True )

    city = models.CharField( max_length=200, blank=True, null=True )
    street = models.CharField( max_length=200, blank=True, null=True )
    country = models.CharField( max_length=200, default='Polska', blank=True, null=True )

    latitude = models.CharField( max_length=50, blank=True, null=True )
    longitude = models.CharField( max_length=50, blank=True, null=True )

    @property
    def address( self ):
        return '%s %s, %s' % ( self.street, self.city, self.country )
    
    @property
    def lat_lng( self ):
        if not self.latitude or not self.longitude:
            try:
                self.latitude, self.longitude = gmaps.address_to_latlng( self.address )
                self.save()
            except Exception, e:
                print "Cannot fetch lat, lng from address: '%s',  %s " % ( self.address, e )
        return self.latitude, self.longitude

# register admin sites
admin.site.register( Type )
admin.site.register( Place )
