from django.shortcuts import render, redirect, get_object_or_404

from address_book.forms import ContactForm
from .models import Contact


def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('contacts_list')


def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        form = ContactForm(instance=contact, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    context = {'form': form}
    return render(request, 'manage_contact.html', context)


def contacts_list(request):
    if request.GET:
        # Handling Search Request for contacts:
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        country = request.GET.get('country')
        city = request.GET.get('city')
        street = request.GET.get('street')
        phone = request.GET.get('phone')
        url = request.GET.get('url')
        contacts_search = {
            'first_name__contains': first_name,
            'last_name__contains': last_name,
            'country__contains': country,
            'city__contains': city,
            'street__contains': street,
            'phone__contains': phone,
            'url__contains': url,
        }
        # Getting rid of None values in contact_search
        contact_search_filtered = {k: v for k, v in contacts_search.items() if v}
        contacts = Contact.objects.filter(**contact_search_filtered)
    else:
        # If there is no search params provided, render all contacts
        contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts_list.html', context)


def add_contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manage_contact.html', context)
