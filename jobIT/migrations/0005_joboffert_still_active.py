# Generated by Django 3.0.4 on 2020-04-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobIT', '0004_auto_20200409_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffert',
            name='still_active',
            field=models.BooleanField(default=True),
        ),
    ]
