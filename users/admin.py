from django.contrib import admin
from .models import Biodata 
# Register your models here.

class BiodataAdmin(admin.ModelAdmin):
    #untuk membuat table yg rapih pada table dashboar admin
    list_display = ('user', 'nama', 'alamat', 'kode_kasir')
    #untuk mencari data pada table dashboard admin
    search_fields = ('user', 'kode_kasir')
    
admin.site.register(Biodata, BiodataAdmin)
