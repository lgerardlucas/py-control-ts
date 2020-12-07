from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    #path('admin/', admin.site.urls),                # adm do site
    path('', admin.site.urls),                      # adm do site até que tenha outro modo de entrada
]
