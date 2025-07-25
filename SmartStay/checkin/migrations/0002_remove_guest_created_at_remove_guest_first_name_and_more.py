# Generated by Django 5.2.4 on 2025-07-16 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='stay_type',
        ),
        migrations.AddField(
            model_name='guest',
            name='name',
            field=models.CharField(default='Dočasné jméno', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guest',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guest',
            name='id_number',
            field=models.CharField(max_length=50),
        ),
    ]
