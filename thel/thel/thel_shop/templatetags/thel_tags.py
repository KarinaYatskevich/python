from django import template
from thel_shop.models import Category
from django.db.models import Count, F

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()





