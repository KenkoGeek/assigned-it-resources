# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='user',
        ),
    ]
