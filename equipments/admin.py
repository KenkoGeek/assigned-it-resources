# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from equipments.models import (
    computerType
)

# Register your models here.

class computerTypeAdmin (admin.ModelAdmin):
    model = computerType
    list_display = ('computersType',)

admin.site.register(computerType, computerTypeAdmin)
