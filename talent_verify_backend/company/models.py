from django.db import models

# Create your models here.
# company/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    date_of_registration = models.DateField()
    company_registration_number = models.CharField(max_length=255)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    email_address = models.EmailField()
    employees = models.ManyToManyField('employees.Employee', related_name='company_employees')

    def __str__(self):
        return self.name