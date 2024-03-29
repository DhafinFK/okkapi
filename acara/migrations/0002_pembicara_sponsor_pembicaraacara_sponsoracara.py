# Generated by Django 5.0.2 on 2024-02-29 14:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acara', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembicara',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PembicaraAcara',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('materi', models.CharField()),
                ('acara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acara.acara')),
                ('pembicara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acara.pembicara')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SponsorAcara',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('package', models.CharField(choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver')], max_length=200)),
                ('acara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acara.acara')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acara.sponsor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
