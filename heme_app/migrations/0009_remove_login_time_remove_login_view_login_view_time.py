# Generated by Django 4.0.5 on 2022-06-07 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('heme_app', '0008_alter_login_time_alter_login_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='time',
        ),
        migrations.RemoveField(
            model_name='login',
            name='view',
        ),
        migrations.AddField(
            model_name='login',
            name='view_Time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
