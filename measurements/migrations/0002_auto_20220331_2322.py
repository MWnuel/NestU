# Generated by Django 3.2.dev20200820070650 on 2022-03-31 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('url', models.URLField(max_length=500)),
                ('lat', models.DecimalField(decimal_places=5, max_digits=20)),
                ('lon', models.DecimalField(decimal_places=5, max_digits=20)),
                ('city', models.TextField(max_length=100)),
                ('country', models.TextField(max_length=100)),
                ('cc', models.TextField(max_length=3)),
                ('sponsor', models.TextField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('host', models.TextField(max_length=200)),
                ('download', models.IntegerField()),
                ('latency', models.DecimalField(decimal_places=5, max_digits=20)),
            ],
        ),
        migrations.AddField(
            model_name='measurements',
            name='server_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='server', to='measurements.server'),
            preserve_default=False,
        ),
    ]