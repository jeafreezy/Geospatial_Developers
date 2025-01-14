# Generated by Django 4.1.2 on 2022-10-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                (
                    "task",
                    models.CharField(
                        db_index=True, help_text="The todo task", max_length=100
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("completed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Todo List",
                "verbose_name_plural": "Todo Lists",
            },
        ),
    ]
