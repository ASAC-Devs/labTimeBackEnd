# Generated by Django 3.2.5 on 2021-07-13 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('tickets', '0004_ta_ta_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
            preserve_default=False,
        ),
    ]
