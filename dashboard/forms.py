from dashboard.models import Kasir, Laporan
from django import forms

class LaporanForms(forms.ModelForm):
    class Meta:
        model = Laporan
        fields = ['nama','upload_file']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
        }
