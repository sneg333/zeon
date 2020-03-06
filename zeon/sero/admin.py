from django.contrib import admin
from .models import *

class MuserAdmin(admin.ModelAdmin):
    list_display = ['id','user_name']
    search_fields = ['id','user_name']


admin.site.register(Muser, MuserAdmin)