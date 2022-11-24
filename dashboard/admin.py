from django.contrib import admin
from .models import *
# Register your models here.
class KasirAdmin(admin.ModelAdmin):
    list_display = ('user','kode')
admin.site.register(Kasir, KasirAdmin)


class LaporanAdmin(admin.ModelAdmin):
    list_display = ('nama','kode_kasir','upload_file','date')
admin.site.register(Laporan, LaporanAdmin)