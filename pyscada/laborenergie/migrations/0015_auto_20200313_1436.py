# Generated by Django 2.2.8 on 2020-03-13 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modbus', '0008_auto_20190206_1507'),
        ('laborenergie', '0014_auto_20200312_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='pysensedevice',
            name='activate_deepsleep',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PySense_activate_deepsleep', to='modbus.ModbusVariable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='activate_deepsleep_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='time_before_deepsleep',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PySense_time_before_deepsleep', to='modbus.ModbusVariable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='time_before_deepsleep_active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
