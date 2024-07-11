from django.shortcuts import render
import csv
import pandas as pd
from django.shortcuts import render, redirect
from .models import Employee
from company.models import Company
import datetime

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Employee
from.forms import EmployeeForm
from django.contrib import messages  # Import the messages module

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    company_id = request.GET.get('company_id')
    if company_id:
        employees = employees.filter(company_id=company_id)
    return render(request, 'employees/employee_list.html', {'employees': employees})

# views.py
from django.shortcuts import render, redirect
from.forms import EmployeeForm


from django.urls import reverse

# employees/views.py
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm
from company.models import Company  # Import the Company model

@login_required
# employees/views.py
# employees/views.py

# talent_verify_backend\employees\views.py
def create_employee(request, company_id):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
            return redirect('company_detail', pk=company_id)
    else:
        form = EmployeeForm()
    return render(request, 'employees/create_employee.html', {'form': form})

@login_required
def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form, 'employee': employee})

# views.py


@login_required
def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('employee_list')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Employee
from.forms import EmployeeForm
import csv
import pandas as pd

@login_required
def update_employee_single(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee_single.html', {'form': form, 'employee': employee})


@login_required



def bulk_update(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_type = file.name.split('.')[-1]
        if file_type == 'csv':
            process_csv_file(file)
        elif file_type == 'xlsx':
            process_excel_file(file)
        return redirect('employee_list')
    return render(request, 'employees/bulk_update.html')

def process_csv_file(file):
    reader = csv.reader(file)
    for row in reader:
        #the CSV
        name, email, phone_number, address, department, job_title, hire_date, company_name, date_of_birth, gender,emergency_contact_name, emergency_contact_phone, emergency_contact_relationship = row
        company, created = Company.objects.get_or_create(
            name=company_name,
            date_of_registration=datetime.date.today()
        )
        Employee.objects.update_or_create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            department=department,
            job_title=job_title,
            hire_date=hire_date,
            company=company,
            date_of_birth=date_of_birth,
            gender=gender,
            emergency_contact_name=emergency_contact_name,
            emergency_contact_phone=emergency_contact_phone,
            emergency_contact_relationship=emergency_contact_relationship
        )

def process_excel_file(file):
    df = pd.read_excel(file)
    for index, row in df.iterrows():
        #theExcel file
        name, email, phone_number, address, department, job_title, hire_date, company_name, date_of_birth, gender, emergency_contact_name, emergency_contact_phone, emergency_contact_relationship = row
        company, created = Company.objects.get_or_create(
            name=company_name,
            date_of_registration=datetime.date.today() 
        )
        Employee.objects.update_or_create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            department=department,
            job_title=job_title,
            hire_date=hire_date,
            company=company,
            date_of_birth=date_of_birth,
            gender=gender,
            emergency_contact_name=emergency_contact_name,
            emergency_contact_phone=emergency_contact_phone,
            emergency_contact_relationship=emergency_contact_relationship
        )

def company_detail(request, pk):
    company = Company.objects.get(pk=pk)
    company_employees = company.employee_set.all()  # Get all employees for this company
    return render(request, 'company/company_detail.html', {'company': company, 'company_employees': company_employees})
from django.shortcuts import render


from . import employee_search

import pandas as pd

class EmployeeDatabase:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)

    def search(self, name):
        return self.df[(self.df['Name'].str.contains(name, case=False)) |
                       (self.df['Company'].str.contains(name, case=False)) |
                       (self.df['Position'].str.contains(name, case=False)) |
                       (self.df['Department'].str.contains(name, case=False))]

import pandas as pd

from django.shortcuts import render
from .models import Employee
from django.db import models

from django.shortcuts import render
from .employee_search import EmployeeDatabase

# views.py
from django.shortcuts import render
from.employee_database import EmployeeDatabase
# views.py
from django.shortcuts import render
from .employee_search import EmployeeDatabase

# views.py
from django.shortcuts import render
from .employee_database import EmployeeDatabase

def employee_search_view(request):
    search_query = request.GET.get('search_query')  # Get the search query from the request
    if search_query:
        employee_db = EmployeeDatabase()  # Initialize EmployeeDatabase without passing a file path
        search_results = employee_db.search(search_query)
        return render(request, 'employees/employee_search_results.html', {'search_results': search_results})
    else:
        return render(request, 'employees/employee_search_form.html')  # Return a form to enter the search query