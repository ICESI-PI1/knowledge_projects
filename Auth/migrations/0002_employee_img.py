# Generated by Django 4.1.7 on 2023-06-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='img',
            field=models.FileField(default='', upload_to='pic/%y/'),
        ),
    ]
