from django.conf.urls import url
from app.vet.base import views

urlpatterns = [
    url(r'^clinicas/$', views.clinica_list),
    url(r'^clinicas/(?P<pk>[0-9]+)/$', views.clinica_detail),
]
