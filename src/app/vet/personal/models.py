# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_administrador = models.BooleanField('Es administrador', default=False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
