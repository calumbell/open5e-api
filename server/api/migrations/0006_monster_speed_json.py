# Generated by Django 2.1 on 2018-09-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180828_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='speed_json',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
