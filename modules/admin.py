from django.contrib import admin
from .models import Modules

class ModulesAdmin(admin.ModelAdmin):
    # Campos que aparecerão ao entrar na model    
    list_display = ('name','menu','system','description','date_create','date_update',)

admin.site.register(Modules,ModulesAdmin)    
