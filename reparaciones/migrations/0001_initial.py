# Generated by Django 3.2.8 on 2022-04-19 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehiculos', '0002_auto_20220418_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=70)),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(decimal_places=0, max_digits=15)),
                ('cantidad', models.IntegerField()),
                ('reparacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reparaciones.reparacion')),
                ('servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reparaciones.servicio')),
            ],
        ),
    ]
