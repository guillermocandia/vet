# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.vet.base import views

urlpatterns = [
    url(r'^clinica/$',
        views.ClinicaDetail.as_view(),
        name='clinica-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
