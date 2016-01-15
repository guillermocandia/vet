# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.recursos.localidades import views

urlpatterns = [
    url(r'^regiones/$',
        views.RegionesList.as_view(),
        name='region-list'),
    url(r'^provincias/$',
        views.ProvinciasList.as_view(),
        name='provincia-list'),
    url(r'^comunas/$',
        views.ComunasList.as_view(),
        name='comuna-list'),
    url(r'^regiones/(?P<pk>[0-9]+)/$',
        views.RegionDetail.as_view(),
        name='region-detail'),
    url(r'^provincias/(?P<pk>[0-9]+)/$',
        views.ProvinciaDetail.as_view(),
        name='provincia-detail'),
    url(r'^comunas/(?P<pk>[0-9]+)/$',
        views.ComunaDetail.as_view(),
        name='comuna-detail')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
