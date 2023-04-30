# Generated by Django 4.2 on 2023-04-28 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=15, verbose_name='Név')),
            ],
        ),
        migrations.CreateModel(
            name='Recept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=60, verbose_name='Név')),
                ('leiras', models.TextField(verbose_name='Leírás')),
                ('kep_eleresi_ut', models.CharField(max_length=255, verbose_name='Kép URL')),
                ('hirdetes_datuma', models.DateField(blank=True, null=True, verbose_name='Hirdetés dátuma')),
                ('kat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kategoria', verbose_name='Kategória')),
            ],
        ),
    ]