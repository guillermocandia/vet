# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.vet.clientes import views

urlpatterns = [
    url(r'^especies/$',
        views.EspecieList.as_view(),
        name='especie-list'),
    url(r'^especies/(?P<pk>[0-9]+)/$',
        views.EspecieDetail.as_view(),
        name='especie-detail'),
    url(r'^razas/$',
        views.RazaList.as_view(),
        name='raza-list'),
    url(r'^razas/(?P<pk>[0-9]+)/$',
        views.RazaDetail.as_view(),
        name='raza-detail'),
    url(r'^especies/(?P<pk>[0-9]+)/razas/$',
        views.EspecieRazaList.as_view(),
        name='especie-raza-list'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
