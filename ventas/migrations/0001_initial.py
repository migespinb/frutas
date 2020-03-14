# Generated by Django 2.2.10 on 2020-03-13 19:45

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
            name='Fruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('cantidad', models.IntegerField()),
                ('precio_compra', models.IntegerField(verbose_name='Precio compra')),
                ('precio_venta', models.IntegerField(verbose_name='Precio venta')),
                ('unidad_medida', models.CharField(max_length=50, null=True, verbose_name='U. Medida')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_total', models.IntegerField(verbose_name='Precio total')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fruta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.Fruta')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=50, null=True, verbose_name='Direccion')),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='Email')),
                ('telefono', models.CharField(max_length=12, null=True, verbose_name='phone')),
                ('imagen', models.ImageField(blank=True, default='defecto.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Abastece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fruta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.Fruta')),
            ],
        ),
    ]