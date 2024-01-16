# Generated by Django 3.1.7 on 2021-07-29 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('comments', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('adresse', models.CharField(max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255)),
                ('nbre', models.IntegerField(blank=True, max_length=255)),
                ('pearson', models.CharField(blank=True, max_length=255)),
                ('responsable', models.CharField(blank=True, max_length=255)),
                ('is_featured', models.BooleanField(blank=True, default=False, null=True)),
                ('publie', models.BooleanField(blank=True, default=False, null=True)),
                ('statut', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demende', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
