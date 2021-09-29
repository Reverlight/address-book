from django.contrib import admin

# Register your models here.
from address_book.models import Contact

admin.site.register(Contact)