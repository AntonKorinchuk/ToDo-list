# Generated by Django 5.0.7 on 2024-07-24 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("marker", "-created")},
        ),
    ]
