from django.urls import path
from .views import * #memanggil semua fungsi 

urlpatterns = [
    path('', list_users,name='list_users'),
]
