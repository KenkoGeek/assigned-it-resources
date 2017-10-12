# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from equipments.models import (
    Computers,
    computerType
)

# Register your models here.

class computerAdmin (admin.ModelAdmin):
    model = Computers
    list_display = ('computersName',)

class computerTypeAdmin (admin.ModelAdmin):
    model = computerType
    list_display = ('computersType',)

admin.site.register(Computers, computerAdmin)
admin.site.register(computerType, computerTypeAdmin)
