from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.vet.base import views

urlpatterns = [
    url(r'^clinicas/$', views.clinica_list),
    url(r'^clinicas/(?P<pk>[0-9]+)/$', views.clinica_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
