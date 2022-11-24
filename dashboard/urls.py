from django.urls import path, include 
from .views import *

urlpatterns = [
     path('', dashboard, name= 'dashboard'),
     
     path('laporan/list/', laporan_list, name='laporan_list'),
     path('laporan/tambah/', laporan_tambah, name='laporan_tambah'),
     path('laporan/update/<int:id_laporan>', laporan_update, name='laporan_update'),
     path('laporan/delete/<int:id>', laporan_delete ,name='laporan_delete'),
     
     # path('user/list', User_list, name='user_list'),
      
     
     
     
     

]