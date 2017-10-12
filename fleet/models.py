# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here.

DATA = (
    ('con data','Si'),
    ('sin data','No')
    )

class Fleet (models.Model):
    phoneModel = models.CharField(max_length=20)
    dataPlan = models.CharField(max_length=8,choices=DATA)

    def __str__(self):
        return '{} {}'.format(self.phoneModel, self.dataPlan)
