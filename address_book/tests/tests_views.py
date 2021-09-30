from unittest import TestCase

from django.test import SimpleTestCase, Client
from django.urls import reverse
from ..models import Contact

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contacts_list_view(self):
        response = self.client.get(reverse('contacts_list'))
        self.assertEquals(response.status_code, 200)

    def test_add_contact_view(self):
        response = self.client.get(reverse('add_contact'))
        self.assertEquals(response.status_code, 200)

    def test_delete_contact_view(self):
        Contact.objects.create(first_name='Don',
                               last_name='Reveys',
                               street='1114 Swick Hill Street',
                               city=' Sugar Land, Texas(TX)',
                               phone='979-925-4196',
                               country='USA'
                               )
        contact = Contact.objects.get(first_name='Don')
        response = self.client.get(reverse('delete_contact', kwargs={'id': contact.id}))
        contact.delete()
        # redirects after deletion
        self.assertEquals(response.status_code, 302)
