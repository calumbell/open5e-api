# Generated by Django 5.1.1 on 2024-10-09 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0006_alter_weapon_range_long_alter_weapon_range_normal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='range_long',
            new_name='long_range',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='range_normal',
            new_name='range',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='range_reach',
            new_name='reach',
        ),
    ]
