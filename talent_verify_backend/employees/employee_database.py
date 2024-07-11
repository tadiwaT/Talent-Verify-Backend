# employee_database.py
from django.db import models
from .models import Employee

class EmployeeDatabase:
    def __init__(self):
        self.employees = Employee.objects.all()

    def search(self, search_query):
        search_results = self.employees.filter(
            models.Q(name__icontains=search_query) |
            models.Q(email__icontains=search_query) |
            models.Q(phone_number__icontains=search_query) |
            models.Q(address__icontains=search_query) |
            models.Q(department__icontains=search_query) |
            models.Q(job_title__icontains=search_query) |
            models.Q(company__name__icontains=search_query)
        )
        return search_results