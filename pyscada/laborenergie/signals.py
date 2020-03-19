# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.models import Device
from pyscada.laborenergie.models import PySenseDevice, ExtendedPySenseDevice

from django.dispatch import receiver
from django.db.models.signals import post_save

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=PySenseDevice)
@receiver(post_save, sender=ExtendedPySenseDevice)
def _reinit_daq_daemons(sender, instance, **kwargs):
    """
    update the daq daemon configuration when changes be applied in the models
    """
    if type(instance) is PySenseDevice:
        post_save.send_robust(sender=Device, instance=instance.PySense_device)
    elif type(instance) is ExtendedPySenseDevice:
        post_save.send_robust(sender=Device, instance=Device.objects.get(pk=instance.pk))
