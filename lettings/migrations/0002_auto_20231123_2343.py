from django.db import migrations

def copy_data_for_lettings(apps, schema_editor):
    # Access the old model
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    # Access the new models
    NewLetting = apps.get_model('lettings', 'Letting')
    Address = apps.get_model('lettings', 'Address')

    # Copy data from old to new
    for old_letting in OldLetting.objects.all():
        # Retrieve or create an Address instance for the new Letting
        new_address, created = Address.objects.get_or_create(
            number=old_letting.address.number,
            street=old_letting.address.street,
            city=old_letting.address.city,
            state=old_letting.address.state,
            zip_code=old_letting.address.zip_code,
            country_iso_code=old_letting.address.country_iso_code,
        )

        # Create a new Letting instance
        NewLetting.objects.create(
            title=old_letting.title,
            address=new_address,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data_for_lettings),
    ]
