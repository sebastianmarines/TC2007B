# Generated by Django 4.2.4 on 2023-10-11 21:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_perfil_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="perfil",
            name="apellido",
        ),
        migrations.RemoveField(
            model_name="perfil",
            name="email",
        ),
        migrations.RemoveField(
            model_name="perfil",
            name="nombre",
        ),
    ]