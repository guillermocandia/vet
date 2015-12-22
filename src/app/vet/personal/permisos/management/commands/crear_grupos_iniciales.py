# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.vet.base.models import Clinica


class Command(BaseCommand):
    args = ''
    help = 'Crea grupos iniciales y define sus permisos por defecto'

    def handle(self, *args, **options):

        group_list = [
                 ('Veterinarios', [
                                  [Clinica,
                                   ['editar_clinica',
                                    'change_clinica']
                                   ],
                                  [Permission,
                                   ['change_permission']
                                   ]
                                  ]
                  ),
                 ('Grupo de prueba', [
                                     [Clinica,
                                      ['add_clinica',
                                       'delete_clinica']
                                      ]
                                     ]
                  )
                 ]

        for group in group_list:
            new_group, created = Group.objects.get_or_create(name=group[0])

            if created:
                self.stdout.write('Grupo %s creado' % group[0])
            else:
                self.stdout.write('Grupo %s ya existe' % group[0])

            new_group.permissions.clear()

            self.stdout.write('Permisos actuales para el grupo %s eliminados'
                              % group[0])

            for c, p in group[1]:
                content_type = ContentType.objects.get_for_model(c)
                for i in p:
                    permission = Permission.objects.get(
                                content_type=content_type, codename=i)
                    new_group.permissions.add(permission)
                    self.stdout.write('Grupo %s: %s añadido' % (group[0], i))
