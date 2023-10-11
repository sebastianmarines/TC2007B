# Generated by Django 4.2.4 on 2023-09-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orgs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="osc",
            options={"verbose_name": "OSC", "verbose_name_plural": "OSCs"},
        ),
        migrations.AlterField(
            model_name="osc",
            name="articulosInteres",
            field=models.ManyToManyField(
                blank=True, related_name="osc_articulos", to="orgs.multimedia"
            ),
        ),
        migrations.AlterField(
            model_name="osc",
            name="imagenes",
            field=models.ManyToManyField(
                blank=True, related_name="osc_imagenes", to="orgs.multimedia"
            ),
        ),
        migrations.AlterField(
            model_name="osc",
            name="videos",
            field=models.ManyToManyField(
                blank=True, related_name="osc_videos", to="orgs.multimedia"
            ),
        ),
    ]
