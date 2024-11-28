from django.contrib import admin
from .models import Galeri

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi_singkat')
    search_fields = ('nama', 'deskripsi_singkat')
