# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department (models.Model):
    departmentName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.departmentName
