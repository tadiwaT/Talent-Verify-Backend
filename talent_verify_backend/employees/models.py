# employees/models.py
from django.db import models
from company.models import Company

class Employee(models.Model):
    # Basic Information
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    # Contact Information
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Job Information
    department = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    hire_date = models.DateField()

    # Company Information
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_employees')
    # Personal Information
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name