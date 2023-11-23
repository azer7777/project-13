from django.db import migrations

def copy_data_for_profiles(apps, schema_editor):
    # Access the old model
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    # Access the new model
    NewProfile = apps.get_model('profiles', 'Profile')

    # Copy data from old to new
    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data_for_profiles),
    ]
