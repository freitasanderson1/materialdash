# Generated by Django 3.0 on 2019-12-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0015_auto_20190719_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='smart',
            field=models.BooleanField(default=True),
        ),
    ]
