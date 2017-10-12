# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class computerType (models.Model):
    computersType = models.CharField(max_length=20)

    def __str__(self):
        return self.computersType

class Computers (models.Model):
    computersName = models.CharField(max_length=40)
    typeName = models.ForeignKey(computerType)

    def __str__(self):
        return '{}, {}'.format(self.typeName, self.computersName)
