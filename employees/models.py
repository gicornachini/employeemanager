# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    department = models.ForeignKey('employees.Department')

    def __unicode__(self):
        return unicode(self.name)


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    def employees_count(self):
        """ Quantidade de empregados no departamento. """
        return self.employee_set.count()
