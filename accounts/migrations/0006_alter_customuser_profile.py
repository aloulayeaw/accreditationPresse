# Generated by Django 5.1.4 on 2025-01-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_reset_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.CharField(blank=True, choices=[('admin', 'admin'), ('groupecentrale', 'groupecentrale'), ('presse', 'presse'), ('freelancer', 'freelancer'), ('cscientifique', 'cscientifique'), ('digital', 'digital')], max_length=255, null=True),
        ),
    ]
