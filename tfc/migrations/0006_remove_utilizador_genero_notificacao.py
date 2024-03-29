# Generated by Django 4.1.2 on 2023-05-25 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tfc", "0005_alter_planta_expo_solar"),
    ]

    operations = [
        migrations.RemoveField(model_name="utilizador", name="genero",),
        migrations.CreateModel(
            name="Notificacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.TextField(default="")),
                ("criticidade", models.IntegerField(default=1)),
                (
                    "planta_associada",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tfc.planta"
                    ),
                ),
            ],
        ),
    ]
