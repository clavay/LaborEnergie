# Generated by Django 2.2.8 on 2020-02-19 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0059_auto_20200211_1049'),
        ('laborenergie', '0003_auto_20200217_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='pysensedevice',
            name='LIS2HH12_acceleration',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LIS2HH12_acceleration', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='LIS2HH12_acceleration_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='LIS2HH12_pitch',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LIS2HH12_pitch', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='LIS2HH12_pitch_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='LIS2HH12_roll',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LIS2HH12_roll', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='LIS2HH12_roll_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='LTR329ALS01_light',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LTR329ALS01_light', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='LTR329ALS01_light_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='PySense_battery',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PySense_battery', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='PySense_battery_voltage_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='SI7006A20_dew_point',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SI7006A20_dew_point', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='SI7006A20_dew_point_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='SI7006A20_humidity',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SI7006A20_humidity', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='SI7006A20_humidity_active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='SI7006A20_temperature',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SI7006A20_temperature', to='pyscada.Variable'),
        ),
        migrations.AddField(
            model_name='pysensedevice',
            name='SI7006A20_temperature_active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
