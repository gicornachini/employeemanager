# -*- coding: utf-8 -*-
from rest_framework import viewsets

from employees.api.serializers import EmployeeSerializer
from employees.models import Employee


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View para obter employee ou uma lista de employees.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
