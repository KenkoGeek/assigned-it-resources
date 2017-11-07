# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from settings.models import Department
# from django.contrib.auth.models import User

from systems.models import (
    Systems,
    Modules,
    Permissions
)

from equipments.models import computerType

from fleet.models import (Fleet)

# Create your models here.

class Worker (models.Model):
    # user = models.ForeignKey(User, blank=True)
    idNumber = models.CharField(max_length=40, unique=True)
    photo = models.ImageField(upload_to='photos/', name=None)
    firstNames = models.CharField(max_length=80)
    lastNames = models.CharField(max_length=80)
    department = models.ForeignKey(Department)
    homePhone = models.CharField(max_length=20)
    celPhone = models.CharField(max_length=20)
    birthPlace = models.CharField(max_length=60)
    systemsAssigned = models.ManyToManyField(Systems, blank=True)
    computerAssigned = models.ManyToManyField(computerType, blank=True)
    fleetAssigned = models.ForeignKey(Fleet, blank=True, null=True)
