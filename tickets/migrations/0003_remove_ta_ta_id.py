# Generated by Django 3.2.5 on 2021-07-13 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ta_ta_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ta',
            name='ta_id',
        ),
    ]
