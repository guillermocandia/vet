from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^base/', include('app.vet.base.urls')),
    url(r'^admin/', include(admin.site.urls))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns = (urlpatterns +
                   static(
                        settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT))
