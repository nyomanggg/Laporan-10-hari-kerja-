# Generated by Django 4.1.1 on 2022-09-27 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kasir',
            options={'verbose_name_plural': 'kasir'},
        ),
        migrations.AlterModelOptions(
            name='laporan',
            options={'verbose_name_plural': 'laporan'},
        ),
    ]
