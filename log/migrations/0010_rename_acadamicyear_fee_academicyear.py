# Generated by Django 3.2 on 2023-09-28 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0009_rename_acadmicyear_fee_acadamicyear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='acadamicyear',
            new_name='academicyear',
        ),
    ]
