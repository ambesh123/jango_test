# Generated by Django 2.1.7 on 2019-02-16 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='isp',
            old_name='rate',
            new_name='price',
        ),
    ]
