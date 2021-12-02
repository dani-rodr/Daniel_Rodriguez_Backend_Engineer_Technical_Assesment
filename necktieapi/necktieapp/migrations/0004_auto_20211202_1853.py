# Generated by Django 3.2.9 on 2021-12-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('necktieapp', '0003_rename_town_address_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='doctor',
        ),
        migrations.AddField(
            model_name='doctor',
            name='contacts',
            field=models.ManyToManyField(to='necktieapp.Contact'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='schedules',
            field=models.ManyToManyField(to='necktieapp.Schedule'),
        ),
    ]