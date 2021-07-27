from django import template
from django.template.defaultfilters import register
from feed.models import RssFeedItems

register = template.Library()


@register.filter
def feed(num_of_results):
    return RssFeedItems.objects.order_by("-created_at")[:num_of_results]
