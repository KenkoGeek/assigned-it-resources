# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from workers.models import Worker


# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    model = Worker
    list_display = ('lastNames', 'firstNames', 'photo')

admin.site.register(Worker, WorkerAdmin)
