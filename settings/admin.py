# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from settings.models import (Department, chiefDepartment)
# Register your models here.

class ChiefDepartmentAdmin(admin.ModelAdmin):
    model = chiefDepartment
    list_display = ('chiefName',)

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display =('departmentName',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(chiefDepartment, ChiefDepartmentAdmin)
