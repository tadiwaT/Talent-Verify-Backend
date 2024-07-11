# talent_verify_backend\employees\EmployeeForm.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone_number', 'address', 'department', 'job_title', 'hire_date', 'date_of_birth', 'gender', 'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship')