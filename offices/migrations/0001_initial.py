# Generated by Django 5.2.2 on 2025-06-27 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('parking_available', models.BooleanField(default=False)),
                ('wifi_speed', models.CharField(blank=True, max_length=50)),
                ('secure_access', models.BooleanField(default=True)),
                ('kitchenette', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_number', models.CharField(max_length=10)),
                ('specs', models.TextField(blank=True)),
                ('available', models.BooleanField(default=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offices.location')),
            ],
        ),
    ]
