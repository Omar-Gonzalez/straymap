# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_raza'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mascotas.Raza'),
            preserve_default=False,
        ),
    ]
