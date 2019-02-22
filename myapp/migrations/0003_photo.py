# Generated by Django 2.1.7 on 2019-02-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190215_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=30, null=True)),
                ('doc', models.FileField(upload_to='documents/')),
            ],
        ),
    ]