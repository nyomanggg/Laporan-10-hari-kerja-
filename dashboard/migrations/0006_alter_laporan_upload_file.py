# Generated by Django 4.1.1 on 2022-10-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_laporan_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporan',
            name='upload_file',
            field=models.FileField(upload_to=''),
        ),
    ]