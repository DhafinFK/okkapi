# Generated by Django 5.0.2 on 2024-02-29 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acara', '0005_alter_acara_pembicara_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoracara',
            name='acara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorship', to='acara.acara'),
        ),
        migrations.AlterField(
            model_name='sponsoracara',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorship', to='acara.sponsor'),
        ),
    ]