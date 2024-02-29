# Generated by Django 5.0.2 on 2024-02-26 07:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BidangKepanitiaan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=200)),
                ('bidang_panitia', models.CharField(choices=[('PI', 'Pengurus Inti'), ('BPH', 'Badan Pengurus Harian')], max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]