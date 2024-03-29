# Generated by Django 5.0.2 on 2024-02-29 02:26

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0006_mentee'),
        ('organisasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rapat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('attendees', models.ManyToManyField(blank=True, related_name='attended_sessions', to='mahasiswa.panitia')),
                ('bidang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rapat', to='organisasi.bidangkepanitiaan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
