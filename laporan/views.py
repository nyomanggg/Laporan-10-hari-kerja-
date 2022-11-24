from django.contrib.auth.models import User
from django.shortcuts import redirect, render #untuk memanggil file html
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
# from dashboard.models import Laporan, Kasir
from dashboard.models import * #format html langsung di tulis di dalam HttpResponse
from users.models import Biodata

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
# @user_passes_test(is_operator)
def base(request):
    template_name = 'base.html'
    context = {
        'title': 'base',
        'welcome' : 'base',
    }
    return render(request, template_name, context)

@login_required
# @user_passes_test(is_operator)
def dashboard(request):
    template_name = "base.html"
    context = {
        'title':'dashboard'
    }
    return render(request, template_name, context)

@login_required
# @user_passes_test(is_operator)
def file_upload(request):
    file_upload = Laporan.objects.all()
    template_name = "forms.html"
    context = {
        'title':'Upload File',
        'file_upload': file_upload,
     }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def User_list(request):
    template_name = 'users.html'
    table = Laporan.objects.all()
    # for a in table:
    #     print(a.nama,'-',a.kode_kasir,'-',a.folder)
    context = {
        'title' : 'table',
        'table': table,
        # 'table':laporan,
    }
    # retrun httpRespon 
    return render(request, template_name, context)


def login (request):
    if request.user.is_authenticated:
        print('sudah login')
        return redirect('dashboard')
    template_name = 'login.html'
    if request.method == "POST":
        # print('POST')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #data ada
            print('username benar')
            auth_login (request, user)
            return redirect('dashboard')
        else:
            #data tidak ada
            print('username salah')
            
    context = {
        'title' : 'login',
    }
    # retrun httpRespon 
    return render(request, template_name, context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def Add_User(request):
    template_name = "add_user.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordconfirmation = request.POST.get('password_confirmation')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        kode_kasir = request.POST.get('kode')
        # try:
        User.objects.create(
            username = username,
            password = password,
            # passwordconfirmation = passwordconfirmation,
            email = email,
            
            # alamat = alamat,
            # kode_kasir = kode_kasir,
            # kode_kasir = kode_kasir
            )
        
        # Kasir.objects.create(
        #     kode_kasir = kode_kasir
        # )
        # Biodata.objects.create(
        #     user = User,
        #     alamat = alamat,
        #     kode_kasir = kode_kasir 
        #     )
        # return redirect(User_list)
        # except:
        #     pass
    context = {
        'title':'Add New User',
     }
    return render(request, template_name, context)