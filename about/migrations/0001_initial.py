# Generated by Django 3.2.8 on 2021-10-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('no_hp', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]