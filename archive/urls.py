

# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to, direct_to_template

entry_pattern = patterns('archive.views',
    (r'^$', 'show'),
    (r'^user/$', 'user'),
    (r'^editmatch/$', 'editmatch'),
    (r'^delete/$', 'delete'),
)

urlpatterns = patterns('archive.views',
    (r'^$', 'index'),
    (r'^new/$', 'new'),
    (r'^contact/$', 'contact'),
    (r'^match/$', 'match'),
    (r'^newmatch/$', 'newmatch'),
    (r'^(?P<slug>[\w\-]+)/', include(entry_pattern)),
)
