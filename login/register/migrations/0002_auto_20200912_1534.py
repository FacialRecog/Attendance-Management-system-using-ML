# Generated by Django 3.0 on 2020-09-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
        migrations.AlterField(
            model_name='register',
            name='age',
            field=models.IntegerField(),
        ),
    ]
