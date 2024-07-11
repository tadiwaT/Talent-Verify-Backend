from django.test import TestCase

# Create your tests here.
# company/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from .models import Company, Employee

class CompanyViewsTestCase(TestCase):
    # ...

    def test_update_company(self):
        response = self.client.post(reverse('update_company', args=[self.company.pk]), {'name': 'Updated Company', 'date_of_registration': '2022-01-01', 'company_registration_number': '9876543210', 'address': '456 Elm St', 'contact_person': 'Jane Doe', 'contact_phone': '987-654-3210', 'email_address': 'jane.doe@example.com'})
        self.assertEqual(response.status_code, 302)