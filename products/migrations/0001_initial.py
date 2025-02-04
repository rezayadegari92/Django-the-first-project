# Generated by Django 4.2.17 on 2024-12-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('available', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Furniture', 'Furniture'), ('Electronic', 'Electronic')], default='null', max_length=10)),
            ],
        ),
    ]
