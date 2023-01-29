from django.shortcuts import render
from django.template.defaulttags import register
from .models import *


def index(request, **kwargs):
    return render(request, 'index.html')


@register.inclusion_tag('menu.html')
def draw_menu(request, menu_name=None, **kwargs):
    if menu_name is not None:
        menu = Menu.objects.filter(name=menu_name)
    else:
        menu = Menu.objects.filter(name="Default")
    menu_items = MenuItem.objects.prefetch_related('menu').filter(menu=menu[0])

    serialized_menu = []
    for menu_item in menu_items:
        serialized_menu.append(menu_item.serializable_object())

    return {'request': request, 'serialized_menu': serialized_menu}


def nav_item(request, slug, **kwargs):
    menu_item = MenuItem.objects.get(slug=slug)
    return render(request, 'nav_item.html', {'nav_item': menu_item})
