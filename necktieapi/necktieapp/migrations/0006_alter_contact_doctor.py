# Generated by Django 3.2.9 on 2021-12-02 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('necktieapp', '0005_auto_20211202_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='necktieapp.doctor'),
        ),
    ]
