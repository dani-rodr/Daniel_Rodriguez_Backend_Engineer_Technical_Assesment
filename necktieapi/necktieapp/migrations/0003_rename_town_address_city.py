# Generated by Django 3.2.9 on 2021-12-02 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('necktieapp', '0002_auto_20211202_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='town',
            new_name='city',
        ),
    ]
