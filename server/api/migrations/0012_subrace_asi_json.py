# Generated by Django 2.1 on 2018-09-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20180921_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='subrace',
            name='asi_json',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
