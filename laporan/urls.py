from django.contrib import admin
from django.urls import path, include

#### untuk media ####
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

### untuk memanggil fungsi home yg ada di dalam dile views
from .views import *
 
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Laporan/user/list', User_list, name='user_list'),
    path('Laporan/add_user/', Add_User, name='add_user'),
    
    #apps
    path('users/',include('users.urls')),
    path('dashboard/',include('dashboard.urls')),
    
    path('',base, name='base'),
    path('file_upload/', file_upload, name='file_upload'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##### untuk media ####
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

