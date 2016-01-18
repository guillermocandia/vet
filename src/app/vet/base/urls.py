# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.vet.base import views

urlpatterns = [
    url(r'^clinica/$',
        views.ClinicaDetail.as_view(),
        name='clinica-detail'),
    url(r'^opcion/$',
        views.OpcionList.as_view(),
        name='opcion-list'),
    url(r'^opcion/(?P<pk>[0-9]+)/$',
        views.OpcionDetail.as_view(),
        name='opcion-detail'),
    url(r'^opcion/(?P<nombre>\S+)/$',
        views.OpcionNombreDetail.as_view(),
        name='opcion-nombre-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
