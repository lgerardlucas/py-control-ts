from django.contrib import admin
from .models import Systems
from modules.models import Modules

class ModulesInline(admin.StackedInline): #TabularInline):
    model = Modules
    max_num = 1 #Information.objects.all().count()
    list_display = ('name','menu','system','description','date_create','date_update',)


class SystemsAdmin(admin.ModelAdmin):
    list_display = ('name','description','date_create','date_update',)
    inlines = (ModulesInline,)

admin.site.register(Systems,SystemsAdmin)    
