# Generated by Django 2.0.5 on 2018-07-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180717_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
