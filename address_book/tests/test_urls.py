from django.urls import reverse, resolve
from ..views import add_contact, edit_contact, delete_contact, contacts_list


class TestUrls:
    def test_add_contact_is_resolved(self):
        url = reverse('add_contact')
        self.assertEquals(resolve(url).func, add_contact)

    def test_edit_contact_is_resolved(self):
        url = reverse('edit_contact', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, edit_contact)

    def test_delete_contact_is_resolved(self):
        url = reverse('delete_contact', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_contact)

    def test_contact_list_is_resolved(self):
        url = reverse('contacts_list')
        self.assertEquals(resolve(url).func, contacts_list)
