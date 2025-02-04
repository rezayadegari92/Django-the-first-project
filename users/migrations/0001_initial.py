# Generated by Django 4.2.17 on 2024-12-31 07:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be 11 digits .', regex='^\\+?1?\\d{11}$')])),
            ],
        ),
    ]
