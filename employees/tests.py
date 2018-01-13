# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db import IntegrityError

from employees.models import Employee, Department


class EmployeeTestCase(TestCase):
    def setUp(self):
        self.marketing = Department.objects.create(name='Marketing')
        self.finance = Department.objects.create(name='Finance')

        self.employee = Employee.objects.create(name='José', email='jose@gmail.com',
                                                department=self.marketing)

    def test_empregados_nao_podem_pertencer_a_dois_departamentos(self):
        """ Um funcionario não deve pertencer a mais de um departamento. """
        self.assertEqual(self.employee.department, self.marketing)

        with self.assertRaises(IntegrityError):
            Employee.objects.create(name='José', email='jose@gmail.com', department=self.finance)
