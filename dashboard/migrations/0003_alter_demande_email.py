# Generated by Django 5.1.4 on 2025-01-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_demande_link_intagram_demande_link_tiktok_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
