# Generated by Django 5.1.3 on 2024-12-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_reporteventa_cambio_reporteventa_monto_pagado'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporteventa',
            name='venta_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
