# company/forms.py
from django import forms
from .models import Company
from employees.models import Employee

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'date_of_registration', 'company_registration_number', 'address', 'contact_person', 'contact_phone', 'email_address')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone_number','address','department', 'job_title', 'hire_date','company' ,'date_of_birth', 'gender', 'emergency_contact_name','emergency_contact_phone','emergency_contact_relationship')