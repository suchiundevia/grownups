# Generated by Django 3.1 on 2020-09-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='qualification',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
