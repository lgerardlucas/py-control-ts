from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static, settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    #path('admin/', admin.site.urls),                # adm do site
    path('', admin.site.urls),                      # adm do site até que tenha outro modo de entrada
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
