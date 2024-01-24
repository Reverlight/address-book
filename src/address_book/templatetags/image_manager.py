from django import template
from django.template.defaultfilters import stringfilter

from core import settings

register = template.Library()


@register.filter
@stringfilter
def get_image_absolute_url(url):
    return f'{settings.MEDIA_URL}/{url}'
