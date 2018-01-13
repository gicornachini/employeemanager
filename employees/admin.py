# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from employees.models import Employee, Department


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'email')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'employees_count')

    def employees_count(self, obj):
        """ Quantidade de employees por departamento. """
        return obj.employees_count()
    employees_count.short_description = 'Employees Count'


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
