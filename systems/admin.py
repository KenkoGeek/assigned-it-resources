# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from systems.models import (
    Systems,
    Modules,
    Permissions
    )
# Register your models here.

class systemsAdmin(admin.ModelAdmin):
    model = Systems
    list_display = ('systemName','systemModules')

class modulesAdmin(admin.ModelAdmin):
    model = Modules
    list_display = ('moduleName',)
    # list_display_links = ('moduleName', 'permission')

class permissionAdmin(admin.ModelAdmin):
    model = Permissions
    list_display = ('permissionName',)

admin.site.register(Systems, systemsAdmin)
admin.site.register(Modules, modulesAdmin)
admin.site.register(Permissions, permissionAdmin)
