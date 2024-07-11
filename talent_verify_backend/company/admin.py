from django.contrib import admin
from django.contrib import admin
from .models import Company
from employees.models import Employee

admin.site.register(Company)
admin.site.register(Employee)