# Generated by Django 2.1.7 on 2019-02-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('mobile', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
            ],
        ),
    ]
