# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from settings.models import (
    maritalStatus,
    bloodType,
    Department
)
# Register your models here.
class MaritalAdmin(admin.ModelAdmin):
    model = maritalStatus
    list_display = ('status',)

class BloodTypeAdmin(admin.ModelAdmin):
    model = bloodType
    list_display = ('type',)

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display =('departmentName',)

admin.site.register(maritalStatus, MaritalAdmin)
admin.site.register(bloodType, BloodTypeAdmin)
admin.site.register(Department, DepartmentAdmin)
