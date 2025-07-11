# Generated by Django 5.2.2 on 2025-06-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialIntegration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('api_key', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
