# Generated by Django 3.2.dev20200820070650 on 2022-04-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0003_rename_server_id_measurements_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField()),
                ('day', models.CharField(choices=[('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday'), ('Al', 'All')], default='Al', max_length=2)),
            ],
        ),
    ]
