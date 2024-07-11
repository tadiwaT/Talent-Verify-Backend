from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Company
from employees.models import Employee
from .forms import CompanyForm
from employees.forms import EmployeeForm

def company_view(request):
    return render(request, 'company/company.html')

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company/create_company.html', {'form': form})

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies})

def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company/update_company.html', {'form': form})

def delete_company(request, pk):
    company = Company.objects.get(pk=pk)
    company.delete()
    return redirect('company_list')

def create_employee(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/create_employee.html', {'form': form, 'company': company})

def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'company/update_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('employee_list')

from django.shortcuts import render
from.models import Company

def company_detail(request, pk):
    company = Company.objects.get(pk=pk)
    company_employees = company.company_employees.all()  # Get all employees for this company
    return render(request, 'company/company_detail.html', {'company': company, 'company_employees': company_employees})

def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'company/employee_detail.html', {'employee': employee})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})