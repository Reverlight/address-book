import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_contact(client):
    with open('address_book/tests/images/Alex.jpg', 'rb') as image:
        response = client.post(reverse('add_contact'), {
            'first_name': 'Alex',
            'last_name': 'Gubanov',
            'country': 'DE',
            'city': 'Berlin',
            'street': 'Hauptstrasse 11',
            'phone': '+496912345678',
            'image': image,

        })
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_delete_contact(client):
    with open('address_book/tests/images/Gleb.png', 'rb') as image:
        create_response = client.post(reverse('add_contact'), {
            'first_name': 'Gleb',
            'last_name': 'Molchun',
            'country': 'GB',
            'city': 'London',
            'street': 'Empire 11',
            'phone': '+442071234567',
            'image': image,
        })
        assert create_response.status_code == 200
    # Created contact always with pk 1 in our test case, so we pass it to deletion
    delete_response = client.post(reverse('delete_contact', args=['1']))
    assert delete_response.status_code == 302


@pytest.mark.django_db
def test_create_get_contacts(client):
    with open('address_book/tests/images/Gleb.png', 'rb') as image:
        create_response = client.post(reverse('add_contact'), {
            'first_name': 'Gleb',
            'last_name': 'Molchun',
            'country': 'GB',
            'city': 'London',
            'street': 'Empire 11',
            'phone': '+442071234567',
            'image': image,
        })
        assert create_response.status_code == 200
    with open('asdaddress_book/tests/images/Alex.jpg', 'rb') as image:
        response = client.post(reverse('add_contact'), {
            'first_name': 'Alex',
            'last_name': 'Gubanov',
            'country': 'DE',
            'city': 'Berlin',
            'street': 'Hauptstrasse 11',
            'phone': '+496912345678',
            'image': image,

        })
    assert response.status_code == 200
    # Test our filter, we have two entries in database (Gleb, Alex),
    # Visible with filter should be only Gleb contact
    response = client.get(reverse('contacts_list') + '?first_name=Gleb&street=Empire 11')
    assert 'First name: Gleb' in str(response.content)
    assert 'Country: United Kingdom' in str(response.content)
    assert 'First name: Alex' not in str(response.content)
    assert 'Country: Germany' not in str(response.content)
