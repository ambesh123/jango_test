# Generated by Django 2.1.7 on 2019-02-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
    ]