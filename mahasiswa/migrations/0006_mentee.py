# Generated by Django 5.0.2 on 2024-02-28 07:51

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kelompok', '0001_initial'),
        ('mahasiswa', '0005_alter_panitia_bidang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jalur_masuk', models.CharField(max_length=100)),
                ('kelompok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kelompok.kelompok')),
                ('mahasiswa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.mahasiswa')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
