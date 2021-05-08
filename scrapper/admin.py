from django.contrib import admin

from .models import diario_as


class AsAdmin(admin.ModelAdmin):
    list_display = ['name', 'point']



admin.site.register(diario_as, AsAdmin)
