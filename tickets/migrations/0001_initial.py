# Generated by Django 3.2.5 on 2021-07-11 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='None')),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.IntegerField(default=None)),
                ('course_name', models.CharField(max_length=256)),
                ('lab_number', models.IntegerField(default=0)),
                ('description', models.TextField(default='enter you question /problem here')),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('closedDate', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(max_length=256)),
                ('rating', models.IntegerField(default=0)),
                ('claimedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.ta')),
                ('raisedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.student')),
            ],
            options={
                'ordering': ['-createdDate'],
            },
        ),
    ]
