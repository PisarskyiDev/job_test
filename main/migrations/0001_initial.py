# Generated by Django 5.0 on 2023-12-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SomeModel",
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
                ("some_name", models.CharField(max_length=255)),
                ("some_value", models.IntegerField()),
            ],
        ),
    ]
