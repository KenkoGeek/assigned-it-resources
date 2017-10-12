# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

PERMISSIONS_NAMES = (
    ("Lectura","Lectura"),
    ("Escritura","Escritura"),
    ("Administrador","Administrador"),
    ("Superusuario","Superusuario")
)

class Permissions (models.Model):
    permissionName = models.CharField(max_length=20, choices=PERMISSIONS_NAMES)

    def __str__(self):
        return self.permissionName


class Modules (models.Model):
    moduleName = models.CharField(max_length=40)
    moduleDesc = models.CharField(max_length=150)
    permission = models.ForeignKey(Permissions)

    def __str__(self):
        return "Permisos de "+"{} en modulo {}".format(self.permission, self.moduleName)


class Systems (models.Model):
    systemName = models.CharField(max_length=30)
    systemModules = models.ForeignKey(Modules)

    def __str__(self):
        return "{}, {}".format(self.systemName, self.systemModules)
