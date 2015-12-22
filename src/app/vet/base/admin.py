# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from .models import Clinica


class ClinicaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo_electronico']

admin.site.register(Clinica, ClinicaAdmin)

admin.site.site_title = settings.CLIENTE_NOMBRE
admin.site.site_header = 'Administración ' + settings.CLIENTE_NOMBRE
