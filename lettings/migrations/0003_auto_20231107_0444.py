# Generated by Django 3.0 on 2023-11-07 03:44

from django.db import migrations

def delete_old_tables(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    OldAddress.objects.all().delete()
    OldLetting.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20231107_0425'),  # Previous migration file for the lettings app
    ]

    operations = [
        migrations.RunPython(delete_old_tables),
    ]

