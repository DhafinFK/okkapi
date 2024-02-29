# Generated by Django 5.0.2 on 2024-02-26 07:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kelompok', '0001_initial'),
        ('okk', '0001_initial'),
        ('organisasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=200)),
                ('npm', models.CharField(max_length=200)),
                ('angkatan', models.PositiveIntegerField(default=2023)),
                ('fakultas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='okk.fakultas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kelompok', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='kelompok.kelompok')),
                ('mahasiswa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.mahasiswa')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Panitia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jabatan', models.CharField(choices=[('PI', 'Pengurus Inti'), ('BPH-PJ', 'BPH - Penanggung Jawab'), ('BPH-WAPJ', 'BPH - Wakil Penanggung Jawab')], max_length=200)),
                ('bidang', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='organisasi.bidangkepanitiaan')),
                ('mahasiswa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.mahasiswa')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]