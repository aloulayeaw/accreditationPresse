# Generated by Django 5.0 on 2023-12-27 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_remove_demande_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="banqueimange",
            name="user",
        ),
        migrations.RemoveField(
            model_name="banqueimangephoto",
            name="user",
        ),
        migrations.RemoveField(
            model_name="banqueressource",
            name="user",
        ),
    ]
