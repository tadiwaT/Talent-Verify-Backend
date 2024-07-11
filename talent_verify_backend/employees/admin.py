from django.contrib import admin
from .models import Employee
# Register your models here.


from django.contrib import admin
from.models import Employee
from.forms import EmployeeForm

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ('name', 'email', 'phone_number', 'address', 'department', 'job_title', 'hire_date', 'get_company', 'date_of_birth', 'gender', 'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship')
    search_fields = ('name', 'email', 'phone_number', 'address', 'department', 'job_title', 'hire_date', 'company_id__name', 'date_of_birth', 'gender', 'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship')
    
    def get_company(self, obj):
        return obj.company_id.name