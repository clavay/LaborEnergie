# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pyscada

__version__ = '0.7.1rc1'
__author__ = 'Camille Lavayssière'

PROTOCOL_ID = 14

parent_process_list = [{'pk': PROTOCOL_ID,
                        'label': 'pyscada.laborenergie',
                        'process_class': 'pyscada.laborenergie.worker.Process',
                        'process_class_kwargs': '{"dt_set":10}',
                        'enabled': True}]


def version():
    return __version__
