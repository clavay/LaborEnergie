# Generated by Django 2.2.8 on 2020-02-19 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborenergie', '0004_auto_20200219_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pysensedevice',
            name='PySense_device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modbus.ModbusDevice'),
        ),
    ]
