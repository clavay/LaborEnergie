# Generated by Django 2.2.8 on 2020-03-12 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modbus', '0008_auto_20190206_1507'),
        ('laborenergie', '0013_auto_20200228_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='pysensedevice',
            name='activity_interrupt_duration',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PySense_activity_interrupt_duration', to='modbus.ModbusVariable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='activity_interrupt_duration_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='activity_interrupt_threshold',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PySense_activity_interrupt_threshold', to='modbus.ModbusVariable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='activity_interrupt_threshold_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='deep_sleep_duration',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PySense_deep_sleep_duration', to='modbus.ModbusVariable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='deep_sleep_duration_active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
