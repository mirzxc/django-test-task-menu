from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('nav_item/<slug:slug>/', views.nav_item, name='nav_item'),
]





