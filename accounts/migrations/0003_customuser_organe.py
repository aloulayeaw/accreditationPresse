# Generated by Django 5.0 on 2023-12-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_customuser_managers_alter_customuser_groups_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="organe",
            field=models.CharField(
                blank=True,
                choices=[("TFM", "TFM"), ("SENEWEB", "SENEWEB"), ("autre", "autre")],
                max_length=255,
                null=True,
            ),
        ),
    ]