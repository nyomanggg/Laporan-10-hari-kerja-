# Generated by Django 4.1.1 on 2022-11-24 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_laporan_kode_kasir'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='kode_kasir',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='dashboard.kasir'),
        ),
    ]
