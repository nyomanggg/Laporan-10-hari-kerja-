# Generated by Django 4.1.1 on 2022-10-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_folder_laporan_upload_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laporan',
            options={'ordering': ['-date'], 'verbose_name_plural': 'laporan'},
        ),
        migrations.AlterField(
            model_name='laporan',
            name='nama',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
