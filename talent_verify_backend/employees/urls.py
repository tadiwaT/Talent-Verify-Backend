
from django.urls import path
from. import views



urlpatterns = [
    path('', views.employee_list, name="employee_list"),
    path('create/<int:company_id>/', views.create_employee, name='create_employee'),
    path('<pk>/update/', views.update_employee, name="update_employee"),
    path('<pk>/delete/', views.delete_employee, name="delete_employee"),
    path('employees/<pk>/update/', views.update_employee_single, name='update_employee_single'),
    path('employees/bulk_update/', views.bulk_update, name='bulk_update'),
    path('employees/search/', views.employee_search_view, name='employee_search'),
    # Remove the login/ pattern
]