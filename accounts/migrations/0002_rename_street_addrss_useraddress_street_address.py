# Generated by Django 4.2.6 on 2024-04-29 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='street_addrss',
            new_name='street_address',
        ),
    ]
