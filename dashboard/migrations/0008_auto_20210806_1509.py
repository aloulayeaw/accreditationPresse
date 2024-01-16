# Generated by Django 3.1.7 on 2021-08-06 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_auto_20210806_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='nbre',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='BanqueRessource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventss', models.CharField(max_length=255)),
                ('commentss', models.CharField(blank=True, max_length=255)),
                ('photo', models.FileField(upload_to='photos/%Y/%m/%d/')),
                ('publie', models.BooleanField(blank=True, default=False, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imageres', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
