# Generated by Django 4.1.5 on 2023-01-26 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("treemenuapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=70, verbose_name="Название меню")),
                (
                    "topics",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="treemenuapp.menuitem",
                    ),
                ),
            ],
        ),
    ]
