from django.conf.urls.defaults import *
from django.contrib.sitemaps import *
from django.conf import settings
from django.conf.urls.defaults import patterns

import logging


log = logging.getLogger('vaschances.urls')


extrapatterns = patterns('')

#The following is used to serve up local media files like images
if getattr(settings, 'LOCAL_DEV', False):
    log.debug("Adding local serving of static files at: %s", settings.STATIC_ROOT)
    baseurlregex = r'^'+settings.STATIC_URL[1:]+'(?P<path>.*)$'
    extrapatterns += patterns('',
        (baseurlregex, 'django.views.static.serve',
        {'document_root':  settings.STATIC_ROOT, 'show_indexes': True})
    )
    log.debug("Adding local serving of media files at: %s", settings.MEDIA_ROOT)
    baseurlregex = r'^'+settings.MEDIA_URL[1:]+'(.*)$'
    extrapatterns += patterns('',
        (baseurlregex, 'django.views.static.serve',
        {'document_root':  settings.MEDIA_ROOT, 'show_indexes': True})
    )

urlpatterns = extrapatterns
