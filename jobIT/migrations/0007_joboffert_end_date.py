# Generated by Django 3.0.4 on 2020-04-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobIT', '0006_auto_20200409_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffert',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
