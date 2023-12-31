# Generated by Django 4.2.5 on 2023-10-09 23:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'categoría de productos',
                'verbose_name_plural': 'categorías de productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True, verbose_name='descripción')),
                ('fecha_actualizacion', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='fecha de actualización')),
                ('categoria_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.productocategoria', verbose_name='categoría')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
