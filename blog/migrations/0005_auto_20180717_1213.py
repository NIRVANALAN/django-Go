# Generated by Django 2.0.5 on 2018-07-17 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='user_name',
            new_name='username',
        ),
    ]