from django.contrib import admin
from .models import Livre, LivreType, LivreStatus

@admin.register(LivreType)
class LivreTypeAdmin(admin.ModelAdmin):
    list_display = ['genre']

@admin.register(LivreStatus)
class LivreStatusAdmin(admin.ModelAdmin):
    list_display = ['status']

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix', 'livre_type', 'livre_status']
    list_filter = ['livre_type', 'livre_status']
    search_fields = ['nom']
