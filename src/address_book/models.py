from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField


class Contact(models.Model):
    class Meta:
        unique_together = ('first_name', 'last_name')

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    country = CountryField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Enter valid phone number, for example: +999999999. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    url_regex = RegexValidator(regex=r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,'
                                     r'6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)',
                               message="Enter valid url, for example: https://www.google.com.ua")
    url = models.CharField(validators=[url_regex], max_length=200, blank=True)

