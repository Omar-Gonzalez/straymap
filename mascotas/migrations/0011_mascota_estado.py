# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-31 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0010_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mascotas.Estado'),
        ),
    ]
