# Generated by Django 3.0 on 2023-11-24 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20231123_2343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
    ]