# Generated by Django 4.2.1 on 2023-05-21 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='senha',
            new_name='password',
        ),
    ]