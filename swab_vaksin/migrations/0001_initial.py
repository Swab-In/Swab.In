# Generated by Django 3.2.8 on 2021-11-05 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SwabInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='-', max_length=25)),
                ('price', models.CharField(default='-', max_length=30)),
                ('akurasi', models.CharField(default='-', max_length=30)),
                ('prosedur', models.CharField(default='-', max_length=50)),
                ('deskripsi', models.TextField(default='-', max_length=500)),
                ('gambar', models.ImageField(default='static\\images\\iSwab.jpg', upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='VaksinInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='-', max_length=25)),
                ('produsen', models.CharField(default='-', max_length=30)),
                ('frekuensi', models.CharField(default='-', max_length=30)),
                ('efikasi', models.CharField(default='-', max_length=30)),
                ('deskripsi', models.TextField(default='-', max_length=500)),
                ('gambar', models.ImageField(default='static\\images\\iVaksin.jpg', upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='VaksinExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pengalamanVaksin', models.TextField(max_length=300)),
                ('penulis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('vaksin_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='swab_vaksin.vaksininformation')),
            ],
        ),
        migrations.CreateModel(
            name='SwabExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pengalamanSwab', models.TextField(max_length=300)),
                ('penulis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('swab_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='swab_vaksin.swabinformation')),
            ],
        ),
    ]
