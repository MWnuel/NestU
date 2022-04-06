# Generated by Django 3.2.dev20200820070650 on 2022-04-01 22:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0004_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='fixedtime',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='use_fixedtime',
            field=models.BooleanField(default=False),
        ),
    ]