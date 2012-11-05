from django.conf.urls.defaults import *
from django.contrib.sitemaps import *
from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import patterns

import logging


log = logging.getLogger('vaschances.urls')


admin.autodiscover()

urlpatterns = getattr(settings, 'URLS', [])

adminpatterns = patterns('',
     (r'^admin/', include(admin.site.urls)),
)


if 'django.contrib.admin' in getattr(settings, 'INSTALLED_APPS', []):
    if urlpatterns:
        urlpatterns += adminpatterns
    else:
        urlpatterns = adminpatterns

#The following is used to serve up local media files like images
if getattr(settings, 'LOCAL_DEV', False):
    log.debug("Adding local serving of static files at: %s", settings.STATIC_ROOT)
    baseurlregex = r'^'+settings.STATIC_URL[1:]+'(?P<path>.*)$'
    urlpatterns += patterns('',
        (baseurlregex, 'django.views.static.serve',
        {'document_root':  settings.STATIC_ROOT, 'show_indexes': True})
    )
    log.debug("Adding local serving of media files at: %s", settings.MEDIA_ROOT)
    baseurlregex = r'^'+settings.MEDIA_URL[1:]+'(.*)$'
    urlpatterns += patterns('',
        (baseurlregex, 'django.views.static.serve',
        {'document_root':  settings.MEDIA_ROOT, 'show_indexes': True})
    )

urlpatterns = urlpatterns + patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^settings/', include('livesettings.urls')),
    (r'^cache/', include('keyedcache.urls')),
)
