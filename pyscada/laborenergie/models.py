# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.modbus.models import ModbusDevice, ModbusVariable
from pyscada.models import Device, Variable, Unit, Scaling
from pyscada.hmi.models import WidgetContentModel
from . import PROTOCOL_ID

from django.db import models

import logging

logger = logging.getLogger(__name__)


class PySenseDevice(WidgetContentModel):
    PySense_device = models.OneToOneField(ModbusDevice, blank=True, null=True, on_delete=models.CASCADE)

    MPL3115A2_temperature = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                              editable=False, related_name='MPL3115A2_temperature')
    MPL3115A2_altitude = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                           editable=False, related_name='MPL3115A2_altitude')
    MPL3115A2_pressure = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                           editable=False, related_name='MPL3115A2_pressure')
    SI7006A20_temperature = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                              editable=False, related_name='SI7006A20_temperature')
    SI7006A20_humidity = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                           editable=False, related_name='SI7006A20_humidity')
    SI7006A20_dew_point = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                            editable=False, related_name='SI7006A20_dew_point')
    SI7006A20_ambient_humidity = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                                   editable=False, related_name='SI7006A20_ambient_humidity')
    LTR329ALS01_light_blue = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                               editable=False, related_name='LTR329ALS01_light_blue')
    LTR329ALS01_light_red = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                              editable=False, related_name='LTR329ALS01_light_red')
    LIS2HH12_acceleration_x = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                                editable=False, related_name='LIS2HH12_acceleration_x')
    LIS2HH12_acceleration_y = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                                editable=False, related_name='LIS2HH12_acceleration_y')
    LIS2HH12_acceleration_z = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                                editable=False, related_name='LIS2HH12_acceleration_z')
    LIS2HH12_roll = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                      editable=False, related_name='LIS2HH12_roll')
    LIS2HH12_pitch = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                       editable=False, related_name='LIS2HH12_pitch')
    battery_voltage = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                        editable=False, related_name='PySense_battery')
    hw_version = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                   editable=False, related_name='PySense_hw_version')
    fw_version = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                   editable=False, related_name='PySense_fw_version')
    product_id = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                   editable=False, related_name='PySense_product_id')
    deep_sleep_duration = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                            editable=False, related_name='PySense_deep_sleep_duration')
    activity_interrupt_threshold = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                                     editable=False,
                                                     related_name='PySense_activity_interrupt_threshold')
    activity_interrupt_duration = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                                    editable=False, related_name='PySense_activity_interrupt_duration')
    activate_deepsleep = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                           editable=False, related_name='PySense_activate_deepsleep')
    time_before_deepsleep = models.ForeignKey(ModbusVariable, blank=True, null=True, on_delete=models.CASCADE,
                                              editable=False, related_name='PySense_time_before_deepsleep')

    MPL3115A2_temperature_active = models.BooleanField(default=False, blank=True)
    MPL3115A2_altitude_active = models.BooleanField(default=False, blank=True)
    MPL3115A2_pressure_active = models.BooleanField(default=False, blank=True)
    SI7006A20_temperature_active = models.BooleanField(default=False, blank=True)
    SI7006A20_humidity_active = models.BooleanField(default=False, blank=True)
    SI7006A20_dew_point_active = models.BooleanField(default=False, blank=True)
    SI7006A20_ambient_humidity_active = models.BooleanField(default=False, blank=True)
    LTR329ALS01_light_blue_active = models.BooleanField(default=False, blank=True)
    LTR329ALS01_light_red_active = models.BooleanField(default=False, blank=True)
    LIS2HH12_acceleration_x_active = models.BooleanField(default=False, blank=True)
    LIS2HH12_acceleration_y_active = models.BooleanField(default=False, blank=True)
    LIS2HH12_acceleration_z_active = models.BooleanField(default=False, blank=True)
    LIS2HH12_roll_active = models.BooleanField(default=False, blank=True)
    LIS2HH12_pitch_active = models.BooleanField(default=False, blank=True)
    battery_voltage_active = models.BooleanField(default=False, blank=True)
    hw_version_active = models.BooleanField(default=False, blank=True)
    fw_version_active = models.BooleanField(default=False, blank=True)
    product_id_active = models.BooleanField(default=False, blank=True)
    deep_sleep_duration_active = models.BooleanField(default=False, blank=True)
    activity_interrupt_threshold_active = models.BooleanField(default=False, blank=True)
    activity_interrupt_duration_active = models.BooleanField(default=False, blank=True)
    activate_deepsleep_active = models.BooleanField(default=False, blank=True)
    time_before_deepsleep_active = models.BooleanField(default=False, blank=True)

    MPL3115A2_temperature_unit = Unit.objects.get_or_create(unit="°C")[0]
    MPL3115A2_altitude_unit = Unit.objects.get_or_create(unit="m")[0]
    MPL3115A2_pressure_unit = Unit.objects.get_or_create(unit="Pa")[0]
    SI7006A20_temperature_unit = Unit.objects.get_or_create(unit="°C")[0]
    SI7006A20_humidity_unit = Unit.objects.get_or_create(unit="%RH")[0]
    SI7006A20_dew_point_unit = Unit.objects.get_or_create(unit="°C")[0]
    SI7006A20_ambient_humidity_unit = Unit.objects.get_or_create(unit="%RH")[0]
    LTR329ALS01_light_blue_unit = Unit.objects.get_or_create(unit="lux")[0]
    LTR329ALS01_light_red_unit = Unit.objects.get_or_create(unit="lux")[0]
    LIS2HH12_acceleration_x_unit = Unit.objects.get_or_create(unit="m.s-2")[0]
    LIS2HH12_acceleration_y_unit = Unit.objects.get_or_create(unit="m.s-2")[0]
    LIS2HH12_acceleration_z_unit = Unit.objects.get_or_create(unit="m.s-2")[0]
    LIS2HH12_roll_unit = Unit.objects.get_or_create(unit="°")[0]
    LIS2HH12_pitch_unit = Unit.objects.get_or_create(unit="°")[0]
    battery_voltage_unit = Unit.objects.get_or_create(unit="V")[0]
    hw_version_unit = Unit.objects.get_or_create(unit="")[0]
    fw_version_unit = Unit.objects.get_or_create(unit="")[0]
    product_id_unit = Unit.objects.get_or_create(unit="")[0]
    deep_sleep_duration_unit = Unit.objects.get_or_create(unit="sec")[0]
    activity_interrupt_threshold_unit = Unit.objects.get_or_create(unit="m.s-2")[0]
    activity_interrupt_duration_unit = Unit.objects.get_or_create(unit="sec")[0]
    activate_deepsleep_unit = Unit.objects.get_or_create(unit="")[0]
    time_before_deepsleep_unit = Unit.objects.get_or_create(unit="sec")[0]

    MPL3115A2_temperature_address = 1
    MPL3115A2_altitude_address = 2
    MPL3115A2_pressure_address = 4
    SI7006A20_temperature_address = 6
    SI7006A20_humidity_address = 8
    SI7006A20_dew_point_address = 10
    SI7006A20_ambient_humidity_address = 12
    LTR329ALS01_light_blue_address = 14
    LTR329ALS01_light_red_address = 15
    LIS2HH12_acceleration_x_address = 16
    LIS2HH12_acceleration_y_address = 18
    LIS2HH12_acceleration_z_address = 20
    LIS2HH12_roll_address = 22
    LIS2HH12_pitch_address = 24
    battery_voltage_address = 26
    hw_version_address = 27
    fw_version_address = 28
    product_id_address = 29
    deep_sleep_duration_address = 30
    activity_interrupt_threshold_address = 31
    activity_interrupt_duration_address = 32
    activate_deepsleep_address = 33
    time_before_deepsleep_address = 34

    MPL3115A2_temperature_function_code = 4
    MPL3115A2_altitude_function_code = 4
    MPL3115A2_pressure_function_code = 4
    SI7006A20_temperature_function_code = 4
    SI7006A20_humidity_function_code = 4
    SI7006A20_dew_point_function_code = 4
    SI7006A20_ambient_humidity_function_code = 4
    LTR329ALS01_light_blue_function_code = 4
    LTR329ALS01_light_red_function_code = 4
    LIS2HH12_acceleration_x_function_code = 4
    LIS2HH12_acceleration_y_function_code = 4
    LIS2HH12_acceleration_z_function_code = 4
    LIS2HH12_roll_function_code = 4
    LIS2HH12_pitch_function_code = 4
    battery_voltage_function_code = 4
    hw_version_function_code = 4
    fw_version_function_code = 4
    product_id_function_code = 4
    deep_sleep_duration_function_code = 3
    activity_interrupt_threshold_function_code = 3
    activity_interrupt_duration_function_code = 3
    activate_deepsleep_function_code = 1
    time_before_deepsleep_function_code = 3

    MPL3115A2_temperature_value_class = 'INT16'
    MPL3115A2_altitude_value_class = 'INT32'
    MPL3115A2_pressure_value_class = 'INT32'
    SI7006A20_temperature_value_class = 'INT32'
    SI7006A20_humidity_value_class = 'INT32'
    SI7006A20_dew_point_value_class = 'INT32'
    SI7006A20_ambient_humidity_value_class = 'INT32'
    LTR329ALS01_light_blue_value_class = 'INT16'
    LTR329ALS01_light_red_value_class = 'INT16'
    LIS2HH12_acceleration_x_value_class = 'INT32'
    LIS2HH12_acceleration_y_value_class = 'INT32'
    LIS2HH12_acceleration_z_value_class = 'INT32'
    LIS2HH12_roll_value_class = 'INT32'
    LIS2HH12_pitch_value_class = 'INT32'
    battery_voltage_value_class = 'INT16'
    hw_version_value_class = 'INT16'
    fw_version_value_class = 'INT16'
    product_id_value_class = 'INT16'
    deep_sleep_duration_value_class = 'INT16'
    activity_interrupt_threshold_value_class = 'INT16'
    activity_interrupt_duration_value_class = 'INT16'
    activate_deepsleep_value_class = 'BOOLEAN'
    time_before_deepsleep_value_class = 'INT16'

    MPL3115A2_temperature_scaling = Scaling.objects.get_or_create(
        description='Divide by 10²', input_low=0, input_high=100, output_low=0, output_high=1, limit_input=False)[0]
    MPL3115A2_altitude_scaling = Scaling.objects.get_or_create(
        description='Divide by 10³', input_low=0, input_high=1000, output_low=0, output_high=1, limit_input=False)[0]
    MPL3115A2_pressure_scaling = Scaling.objects.get_or_create(
        description='Divide by 10¹', input_low=0, input_high=10, output_low=0, output_high=1, limit_input=False)[0]
    SI7006A20_temperature_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁵', input_low=0, input_high=100000, output_low=0, output_high=1, limit_input=False)[0]
    SI7006A20_humidity_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁵', input_low=0, input_high=100000, output_low=0, output_high=1, limit_input=False)[0]
    SI7006A20_dew_point_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁵', input_low=0, input_high=100000, output_low=0, output_high=1, limit_input=False)[0]
    SI7006A20_ambient_humidity_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁵', input_low=0, input_high=100000, output_low=0, output_high=1, limit_input=False)[0]
    LTR329ALS01_light_blue_scaling = None
    LTR329ALS01_light_red_scaling = None
    LIS2HH12_acceleration_x_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁶', input_low=0, input_high=1000000, output_low=0, output_high=1, limit_input=False)[0]
    LIS2HH12_acceleration_y_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁶', input_low=0, input_high=1000000, output_low=0, output_high=1, limit_input=False)[0]
    LIS2HH12_acceleration_z_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁶', input_low=0, input_high=1000000, output_low=0, output_high=1, limit_input=False)[0]
    LIS2HH12_roll_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁶', input_low=0, input_high=1000000, output_low=0, output_high=1, limit_input=False)[0]
    LIS2HH12_pitch_scaling = Scaling.objects.get_or_create(
        description='Divide by 10⁶', input_low=0, input_high=1000000, output_low=0, output_high=1, limit_input=False)[0]
    battery_voltage_scaling = Scaling.objects.get_or_create(
        description='Divide by 10²', input_low=0, input_high=100, output_low=0, output_high=1, limit_input=False)[0]
    hw_version_scaling = None
    fw_version_scaling = None
    product_id_scaling = None
    deep_sleep_duration_scaling = None
    activity_interrupt_threshold_scaling = None
    activity_interrupt_duration_scaling = None
    activate_deepsleep_scaling = None
    time_before_deepsleep_scaling = None

    def save(self, **kwargs):
        super(PySenseDevice, self).save(**kwargs)
        for field in self._meta.fields:
            if field.get_internal_type() == "ForeignKey" and getattr(self, str(field).split('.')[-1]) is None:
                new_var = Variable.objects.get_or_create(
                    name=self.PySense_device.modbus_device.short_name + "_" + self._meta.object_name + "_" +
                    str(field).split('.')[-1],
                    description=self.PySense_device.modbus_device.short_name + "_" + self._meta.object_name + "_"
                    + str(field).split('.')[-1],
                    short_name=str(field).split('.')[-1],
                    device=self.PySense_device.modbus_device,
                    value_class=getattr(self, str(field).split('.')[-1] + "_value_class"),
                    scaling=getattr(self, str(field).split('.')[-1] + "_scaling"),
                    unit=getattr(self, str(field).split('.')[-1] + "_unit"),
                    writeable=True if getattr(self, str(field).split('.')[-1] + "_function_code") == 3 else True if
                    getattr(self, str(field).split('.')[-1] + "_function_code") == 1 else False)
                setattr(self,
                        str(field).split('.')[-1],
                        ModbusVariable.objects.get_or_create(
                            modbus_variable_id=new_var[0].id,
                            address=getattr(self, str(field).split('.')[-1] + "_address"),
                            function_code_read=getattr(self, str(field).split('.')[-1] + "_function_code"))[0]
                        )

            if field.get_internal_type() == "BooleanField" and '_active' in field.name:
                Variable.objects.filter(name__contains=field.name.replace('_active', '')).\
                    update(active=getattr(self, str(field).split('.')[-1]))

    protocol_id = PROTOCOL_ID

    def parent_device(self):
        try:
            return self.PySense_device.parent_device()
        except:
            return None

    def __str__(self):
        return self.PySense_device.modbus_device.short_name

    def visible(self):
        return True

    def gen_html(self, **kwargs):
        """

        :return: main panel html and sidebar html as
        """
        # main_template = get_template('DUT_selector.html')
        main_content = None  # main_template.render(dict(dut_selector=self))
        sidebar_content = None
        return main_content, sidebar_content


class ExtendedPySenseDevice(Device):
    class Meta:
        proxy = True
        verbose_name = 'PySense Device'
        verbose_name_plural = 'PySense Devices'
