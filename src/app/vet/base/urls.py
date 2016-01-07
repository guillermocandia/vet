from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.vet.base import views

urlpatterns = [
    url(r'^clinicas/$', views.ClinicaList.as_view()),
    url(r'^clinicas/(?P<pk>[0-9]+)/$', views.ClinicaDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
