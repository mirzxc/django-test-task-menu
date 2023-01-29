from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=70, verbose_name="Название меню")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=70, verbose_name="Категория меню")
    slug = models.SlugField(max_length=100, unique=True, verbose_name='url')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True,
                             null=True, related_name='menu')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('nav_item', kwargs=kwargs)

    def serializable_object(self):
        obj = {'title': self.title, 'slug': self.slug, 'children': []}
        for child in self.children.all():
            obj['children'].append(child.serializable_object())
        return obj
