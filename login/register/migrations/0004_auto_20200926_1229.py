# Generated by Django 3.0 on 2020-09-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_register_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
