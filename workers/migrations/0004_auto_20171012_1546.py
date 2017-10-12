# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
        ('equipments', '0001_initial'),
        ('workers', '0003_worker_fleetassigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='computerAssigned',
            field=models.ManyToManyField(to='equipments.Computers'),
        ),
        migrations.AddField(
            model_name='worker',
            name='systemsAssigned',
            field=models.ManyToManyField(to='systems.Systems'),
        ),
    ]
