# Generated by Django 2.2.8 on 2020-02-19 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laborenergie', '0008_auto_20200219_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pysensedevice',
            old_name='PySense_battery_voltage',
            new_name='battery_voltage',
        ),
        migrations.RenameField(
            model_name='pysensedevice',
            old_name='PySense_battery_voltage_active',
            new_name='battery_voltage_active',
        ),
    ]