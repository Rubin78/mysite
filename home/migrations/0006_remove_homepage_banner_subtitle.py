# Generated by Django 3.1.3 on 2020-11-17 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_subtitle',
        ),
    ]
