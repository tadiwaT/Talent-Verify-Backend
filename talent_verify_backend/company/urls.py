# company/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.company_view, name="company"),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('', views.company_list, name="company_list"),
    path('companies/create/', views.create_company, name="create_company"),
    path('companies/<pk>/update/', views.update_company, name="update_company"),
    path('companies/<pk>/delete/', views.delete_company, name="delete_company"),
    path('employees/', views.employee_list, name="employee_list"),
    path('create/<int:company_id>/', views.create_employee, name='create_employee'),
    path('companies/<int:company_pk>/create_employee/', views.create_employee, name='create_employee'),
    path('employees/<pk>/update/', views.update_employee, name="update_employee"),
    path('employees/<pk>/delete/', views.delete_employee, name="delete_employee"),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),  # Add this line
    
]


