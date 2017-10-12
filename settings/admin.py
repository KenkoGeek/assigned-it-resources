# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from settings.models import (Department)
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display =('departmentName',)

admin.site.register(Department, DepartmentAdmin)
