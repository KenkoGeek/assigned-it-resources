# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleName', models.CharField(max_length=40)),
                ('moduleDesc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systemName', models.CharField(max_length=30)),
                ('systemModules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.Modules')),
            ],
        ),
    ]
