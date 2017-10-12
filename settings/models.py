# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department (models.Model):
    departmentName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.departmentName


class maritalStatus (models.Model):
    status = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.status

class bloodType (models.Model):
    type = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.type
