# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from fleet.models import Fleet

# Register your models here.
class FleetAdmin (admin.ModelAdmin):
    model = Fleet
    list_display = ('phoneModel','dataPlan')

admin.site.register(Fleet, FleetAdmin)
