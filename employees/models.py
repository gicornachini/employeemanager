# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    department = models.ForeignKey('employees.Department')


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)