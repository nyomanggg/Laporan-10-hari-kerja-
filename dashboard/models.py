from sre_parse import Verbose
from turtle import mode
from django.db import models 
from django.contrib.auth.models import User


# Create your models here.
class Kasir (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kasir', blank=True, null=True)
    kode = models.CharField(max_length=10)
    
    def __str__(self):
        return self.kode
    
    class Meta: 
        verbose_name_plural = "kasir"
    
class Laporan(models.Model):
    nama = models.CharField(max_length=100, blank=False, null=False)
    kode_kasir = models.ForeignKey(Kasir, on_delete=models.CASCADE, related_name='laporan')
    # folder nanti di rubah jadi upload file (jangan lupa di file adminnya juga)
    upload_file = models.FileField(upload_to='file/', null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.kode_kasir)
    
    class Meta: 
        ordering = ['-date']
        verbose_name_plural = "laporan"     