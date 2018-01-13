# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from employees.api import views as api_views

urlpatterns = [
    url(r'^$', api_views.EmployeeViewSet.as_view({'get': 'list'}), name='list'),
]
