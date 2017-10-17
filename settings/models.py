# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class chiefDepartment (models.Model):
    chiefName = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.chiefName


class Department (models.Model):
    departmentName = models.CharField(max_length=50, unique=True)
    chief = models.ForeignKey(chiefDepartment)

    def __str__(self):
        return "{}, {}".format(self.departmentName, self.chief)
