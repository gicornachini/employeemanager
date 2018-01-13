# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from model_mommy import mommy

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

    def test_obter_a_quantidade_de_funcionarios_por_setor(self):
        """ Obter a quantidade de funcionarios por departamento. """
        markt_employee_2 = mommy.make(Employee, department=self.marketing)
        markt_employee_3 = mommy.make(Employee, department=self.marketing)

        finance_employee_4 = mommy.make(Employee, department=self.finance)
        self.assertTrue(self.marketing.employees_count(), 3)
        self.assertTrue(self.finance.employees_count(), 2)
