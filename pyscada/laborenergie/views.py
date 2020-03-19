# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.conf import settings

import logging

logger = logging.getLogger(__name__)

UNAUTHENTICATED_REDIRECT = settings.UNAUTHENTICATED_REDIRECT if hasattr(
    settings, 'UNAUTHENTICATED_REDIRECT') else '/accounts/login/'


def unauthenticated_redirect(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.is_authenticated:
            return redirect('%s?next=%s' % (UNAUTHENTICATED_REDIRECT, args[0].path))
        return func(*args, **kwargs)
    return wrapper
