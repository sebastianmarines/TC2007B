# Generated by Django 4.2.4 on 2023-09-27 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OSC',
            fields=[
                ('oscId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('coordenadas_latitud', models.FloatField()),
                ('coordenadas_longitud', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('areaContacto', models.CharField(max_length=255)),
                ('horaAtencion', models.CharField(max_length=255)),
                ('paginaWeb', models.URLField()),
                ('redesSociales', models.JSONField()),
                ('articulosInteres', models.ManyToManyField(related_name='osc_articulos', to='orgs.multimedia')),
                ('imagenes', models.ManyToManyField(related_name='osc_imagenes', to='orgs.multimedia')),
                ('tags', models.ManyToManyField(to='orgs.tag')),
                ('videos', models.ManyToManyField(related_name='osc_videos', to='orgs.multimedia')),
            ],
        ),
    ]