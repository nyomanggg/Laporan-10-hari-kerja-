from tabnanny import verbose
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from numpy import true_divide
from dashboard.models import Kasir

#create model 

class Biodata(models.Model):
    #cascade berarti ketika user di dalet biodata akan terhapus
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
    alamat = models.TextField(blank=True, null=True)
    # kode_kasir = models.CharField( max_length=5 )
    kode_kasir = models.CharField(max_length=10)
    
    def __str__(self):
        return "{}".format(self.nama)
    
    #agar penulisan didasboar admin tidak ada penambahan s seperti biodatas
    class Meta: 
        verbose_name_plural = "Biodata"
        
