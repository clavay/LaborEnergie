# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

urlpatterns = [
    # Public pages
    url(r'^nested_admin/', include('nested_admin.urls')),
]
