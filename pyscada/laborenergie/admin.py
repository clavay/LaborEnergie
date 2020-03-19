# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.modbus import PROTOCOL_ID
from pyscada.modbus.models import ModbusDevice

from pyscada.laborenergie.models import PySenseDevice, ExtendedPySenseDevice
from pyscada.admin import admin_site
from pyscada.models import DeviceProtocol
import nested_admin

import logging

logger = logging.getLogger(__name__)


class PySenseDeviceAdminInline(nested_admin.NestedStackedInline):
    model = PySenseDevice


class PySenseModbusDeviceAdminInline(nested_admin.NestedStackedInline):
    model = ModbusDevice

    inlines = [
        PySenseDeviceAdminInline,
    ]


class PySenseDeviceAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id', 'short_name')
    list_display_links = ('id', 'short_name')

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'byte_order':
            db_field.default = '3-2-1-0'
        return super(PySenseDeviceAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'protocol':
            kwargs['queryset'] = DeviceProtocol.objects.filter(pk=PROTOCOL_ID)
            db_field.default = PROTOCOL_ID
        return super(PySenseDeviceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(PySenseDeviceAdmin, self).get_queryset(request)
        return qs.filter(protocol_id=PROTOCOL_ID)

    inlines = [
        PySenseModbusDeviceAdminInline,
    ]


admin_site.register(ExtendedPySenseDevice, PySenseDeviceAdmin)
