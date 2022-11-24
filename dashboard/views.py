#from decimal import ConversionSyntax
from re import template
from winreg import REG_QWORD
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from matplotlib.style import context
from dashboard.admin import LaporanAdmin
from dashboard.models import Laporan
from dashboard.forms import LaporanForms 

from django.http import HttpResponse
from .models import *
#Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
       return True
    else:
        return False
def is_kasir(user):
    if user.groups.filter(name='Kasir').exists():
        return True
    else:
        return False
    
@login_required
def dashboard(request):
    template_name = 'base.html'
    context = {
        'title': 'dashboard',
        'welcome' : 'dashboard',
    }
    return render(request, template_name, context)

@login_required
def laporan_list(request):
    template_name = 'laporan.html'
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

@login_required
# @user_passes_test(is_kasir)
def laporan_tambah (request):
    template_name = 'forms.html'
    if request.method == "POST":
        forms = LaporanForms(request.POST, request.FILES)
        if forms.is_valid():
            data = forms.save(commit=False)
            data.kode_kasir = request.user.kasir
            data.save()
            return redirect(laporan_list)
    else:
        forms = LaporanForms()
    context = {
        'title' : 'form laporan',
        'welcome' : 'laporan',
        'forms' : forms
        
    }
    return render(request, template_name, context)

@login_required
def laporan_update(request, id_laporan):
    template_name = 'forms.html'
    laporan = Laporan.objects.get(id=id_laporan)
    if request.method == "POST":
        forms = LaporanForms(request.POST, request.FILES, instance=laporan)
        if forms.is_valid():
            data = forms.save(commit=False)
            data.kode_kasir = request.user.kasir
            data.save()
            return redirect(laporan_list)
    else:
        forms = LaporanForms(instance=laporan)
    context = {
        'title' : 'form laporan',
        'welcome' : 'laporan',
        'forms' : forms
        
    }
    return render(request, template_name, context)

@login_required
# @user_passes_test(is_operator)
def User_list(request):
    template_name = 'users.html'
    table = Laporan.objects.all()
    for a in table:
     #     print(a.nama,'-',a.kode_kasir,'-',a.folder)
     context = {
         'title' : 'table',
         'table': table,
         # 'table':laporan,
     }
#     # retrun httpRespon 
     return render(request, template_name, context)


#fitur delete
@login_required
def laporan_delete (request, id):
    Laporan.objects.get(id=id).delete()
    return redirect(laporan_list)
# melihat detail info file yang di upload
# def lihat_file (request, id):
#     template_name = "front/lihat.html"
#     Laporan = laporan.objects.get(id=id)
#     # print(Laporan)
#     context = {
#         'title' : 'lihat file',   
#         'Laporan': Laporan,    
#     }
#     return render(request, template_name, context)
    
