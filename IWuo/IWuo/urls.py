from django.conf.urls import patterns, include, url
from IWuo.views import hello
from IWuo.views import mytime


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IWuo.views.home', name='home'),
    # url(r'^IWuo/', include('IWuo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^hello/$',hello),
    ('^mytime/$',mytime),
)
