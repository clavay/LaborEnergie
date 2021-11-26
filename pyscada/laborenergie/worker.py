#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from pyscada.utils.scheduler import SingleDeviceDAQProcessWorker
from pyscada.laborenergie import PROTOCOL_ID

import logging

logger = logging.getLogger(__name__)


class Process(SingleDeviceDAQProcessWorker):
    device_filter = dict(modbusdevice__pysensedevice__isnull=False, protocol_id=PROTOCOL_ID)
    bp_label = 'pyscada.laborenergie-%s'

    def __init__(self, dt=5, **kwargs):
        super(SingleDeviceDAQProcessWorker, self).__init__(dt=dt, **kwargs)

    def init_process(self):
        pass

    def loop(self):
        return 1, None
